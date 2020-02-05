qry_insert = {"tb_user":"", "tb_user_background":"", "tb_topic":"", "tb_evaluate":"", "tb_dashboard":"", "tb_chart":"", "tb_topic_chart":"", "tb_dashboard_topic_chart":"", "tb_question_dashboard":""}
qry_insert["tb_user"] = """INSERT INTO tb_user (cl_name, cl_record_date) VALUES (?,?);"""
qry_insert["tb_user_background"] = """INSERT INTO tb_user_background (cl_user_id) VALUES (?);"""
qry_insert["tb_topic"] = """INSERT INTO tb_topic (cl_label) VALUES (?);"""
qry_insert["tb_evaluate"] = """INSERT INTO tb_evaluate (cl_user_id, cl_topic_id, cl_value) VALUES (?,?,?);"""
qry_insert["tb_dashboard"] = """INSERT INTO tb_dashboard (cl_user_id, cl_name, cl_type, cl_language, cl_record_date) VALUES (?,?,?,?,?);"""
qry_insert["tb_chart"] = """INSERT INTO tb_chart (cl_chart_value) VALUES (?);"""
qry_insert["tb_topic_chart"] = """INSERT INTO tb_topic_chart (cl_chart_id, cl_topic_id) VALUES (?,?);"""
qry_insert["tb_dashboard_topic_chart"] = """INSERT INTO tb_dashboard_topic_chart (cl_dashboard_id, cl_topic_chart_id, cl_order, cl_feedback, cl_active) VALUES (?,?,?,?,?);"""
qry_insert["tb_question_dashboard"] = """INSERT INTO tb_question_dashboard (cl_dashboard_id, cl_feedback, cl_important, cl_not_important) VALUES (?,?,?,?);"""

## SELECT PARAM
# qry_select["user"] -> (user id)
# qry_select["dashboard"] -> (user id, dashboard type)
# qry_select["topics_charts"] -> (topic id)
# qry_select["topic_chart_id"] -> (topic id, chart id)
# qry_select["topics"] -> (topic id)
# qry_select["chart"] -> (chart value)
# qry_select["user_dashboard_charts"] -> (user id, dashboard id, dashboard type, topic id, chart id)
# qry_select["user_dashboard_charts_active"] -> (user id, dashboard id, dashboard type)
# qry_select["user_dashboard_charts_active_by_topic"] -> (user id, dashboard id, dashboard type, topic id)
# qry_select["user_dashboard_charts_active_by_topic_chart"] -> (user id, dashboard id, dashboard type, topic id, chart id)
# qry_select["prev_user_dashboard_charts_active_by_topic_chart"] -> (user id, dashboard id, dashboard type, order)
# qry_select["next_user_dashboard_charts_active_by_topic_chart"] -> (user id, dashboard id, dashboard type, order)

qry_select = {"user":"", "dashboard":"", "topics_charts": "", "topic_chart_id": "", "topics": "", "chart": "", "user_dashboard_charts": "", "user_dashboard_charts_active": "", "user_dashboard_charts_active_by_topic": "", "user_dashboard_charts_active_by_topic_chart": "", "prev_user_dashboard_charts_active_by_topic_chart": "", "next_user_dashboard_charts_active_by_topic_chart": ""}

## Select user;
qry_select["user"] = """SELECT * 
                            FROM tb_user 
                            WHERE cl_id = ?"""

## Select user dashboard [Fixo: cl_type = 0; Customizável: cl_type = 1]
qry_select["dashboard"] = """SELECT * 
                                FROM tb_dashboard 
                                WHERE cl_user_id = ? and cl_type = ?;"""

## Select charts from a topic
qry_select["topics_charts"] = """SELECT b.cl_chart_value 
                                    FROM tb_topic_chart a 
                                            inner join tb_chart b on a.cl_chart_id = b.cl_id 
                                    WHERE cl_topic_id = ?
                                    ORDER BY b.cl_id;"""

## Select id from tb_topic_chart
qry_select["topic_chart_id"] = """SELECT cl_id
                                    FROM tb_topic_chart
                                    WHERE cl_topic_id = ? and cl_chart_id = ?"""

## Select label from a topic
qry_select["topics"] = """SELECT cl_label 
                            FROM tb_topic 
                            WHERE cl_id = ?;"""

## Select chart id from a cl_chart_value
qry_select["chart"] = """SELECT cl_id 
                            FROM tb_chart 
                            WHERE cl_chart_value = ?;"""

## Select user charts and topics from dashboard;
qry_select["user_dashboard_charts"] = """SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, f.cl_id, e.cl_chart_value, c.cl_active
                                            FROM tb_user a 
                                                    inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                    inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                    inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                    inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                    inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                            WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and d.cl_topic_id = ? and d.cl_chart_id = ?
                                            ORDER BY c.cl_order;"""

## Select user charts and topics active from dashboard;
qry_select["user_dashboard_charts_active"] = """SELECT b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, f.cl_id, e.cl_chart_value
                                                    FROM tb_user a 
                                                            inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                            inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                            inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                            inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                            inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                    WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and c.cl_active = 1
                                                    ORDER BY c.cl_order;"""

## Select max order from dashboard;
qry_select["max_order_user_dashboard_charts"] = """SELECT max(c.cl_order)
                                                    FROM tb_user a 
                                                            inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                            inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                            inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                            inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                            inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                    WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ?"""

## Select user charts active from dashboard specifying the topic;
qry_select["user_dashboard_charts_active_by_topic"] = """SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, e.cl_chart_value
                                                            FROM tb_user a 
                                                                    inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                                    inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                                    inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                                    inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                                    inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                            WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and d.cl_topic_id = ? and c.cl_active = 1
                                                            ORDER BY c.cl_order;"""

## Select user charts active from dashboard specifying the topic and chart;
qry_select["user_dashboard_charts_active_by_topic_chart"] = """SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, e.cl_chart_value
                                                                FROM tb_user a 
                                                                        inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                                        inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                                        inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                                        inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                                        inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                                WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and d.cl_topic_id = ? and d.cl_chart_id = ? and c.cl_active = 1
                                                                ORDER BY c.cl_order;"""

## Select previous user charts active from dashboard specifying the topic and chart order;
qry_select["prev_user_dashboard_charts_active_by_topic_chart"] = """SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, e.cl_chart_value
                                                                        FROM tb_user a 
                                                                                inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                                                inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                                                inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                                                inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                                                inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                                        WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and c.cl_order < ? and c.cl_active = 1
                                                                        ORDER BY c.cl_order DESC;"""

## Select next user charts active from dashboard specifying the topic and chart order;
qry_select["next_user_dashboard_charts_active_by_topic_chart"] = """SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, e.cl_chart_value
                                                                        FROM tb_user a 
                                                                                inner join tb_dashboard b on a.cl_id = b.cl_user_id 
                                                                                inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id 
                                                                                inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id 
                                                                                inner join tb_chart e on d.cl_chart_id = e.cl_id 
                                                                                inner join tb_topic f on d.cl_topic_id = f.cl_id 
                                                                        WHERE b.cl_user_id = ? and c.cl_dashboard_id = ? and b.cl_type = ? and c.cl_order > ? and c.cl_active = 1
                                                                        ORDER BY c.cl_order;"""

## UPDATE PARAM
# qry_update["dashboard_charts_active"] -> SET(active) WHERE(dashboard_topic_chart id)
# qry_update["dashboard_charts_order"] -> SET(order) WHERE(dashboard_topic_chart id)

qry_update = {"dashboard_charts_active":"","dashboard_charts_order":""}
qry_update["dashboard_charts_active"] = """UPDATE tb_dashboard_topic_chart
                                            SET cl_active = ?
                                            WHERE cl_id = ?"""

qry_update["dashboard_charts_order"] = """UPDATE tb_dashboard_topic_chart
                                            SET cl_order = ?
                                            WHERE cl_id = ?"""

# SELECT c.cl_id, b.cl_user_id, a.cl_name, b.cl_name, c.cl_order, f.cl_label, e.cl_chart_value FROM tb_user a inner join tb_dashboard b on a.cl_id = b.cl_user_id inner join tb_dashboard_topic_chart c on b.cl_id = c.cl_dashboard_id inner join tb_topic_chart d on c.cl_topic_chart_id = d.cl_id inner join tb_chart e on d.cl_chart_id = e.cl_id inner join tb_topic f on d.cl_topic_id = f.cl_id 
# WHERE b.cl_user_id = 1 and c.cl_dashboard_id = 2 and b.cl_type = 1 and d.cl_topic_id = 8 and c.cl_active = 1 ORDER BY c.cl_order;