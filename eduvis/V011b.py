import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State
import pandas as pd

import visdcc

app = dash.Dash()

def getNodesFromCsv(name):
	array = []
	
	conteudo = pd.read_csv(name, header = 0, index_col = 0)

	i = len(conteudo.dropna())

	for item in conteudo.iterrows():
		dic = {}
		if item[0] < i:
			dic.update({'id': item[1][0], 'label': item[1][1], 'color': item[1][2], 'level': item[1][5], 'font': {'size': int(item[1][6][:2])}})

			if item[1][6][4:]:
				dic['font']['color'] = item[1][6][4:]

			a = conteudo['shape'] != '-'
			if (a[item[0]]):
				dic.update({'shape': item[1][3], 'size': item[1][4]})
			
			array.append(dic)
	
	return array


def getEdgesFromCsv(name):
	array = []
	
	conteudo = pd.read_csv(name, header = 0, index_col = 0)

	i = len(conteudo.dropna())

	for item in conteudo.iterrows():
		dic = {}
		if item[0] < i:
			dic.update({'id': item[1][0], 'from': item[1][2], 'to': item[1][3]})

			a = conteudo['hidden'] != '-'
			if (a[item[0]]):
				dic.update({'hidden': item[1][4]})

			b = conteudo['width'] != '-'
			if (b[item[0]]):
				dic.update({'width': item[1][5]})

			c = conteudo['arrows'] != '-'
			if (c[item[0]]):
				dic.update({'arrows': item[1][1]})
			
			array.append(dic)
	
	return array


app.layout = html.Div([
                visdcc.Network(id='net',
                        data={
                                'nodes': getNodesFromCsv('V011b-nodes.csv'),

                                'edges': getEdgesFromCsv('V011b-edges.csv')
                        },

                        options={'height':'600px',
                                        'width':'100%',
                                        'layout':{'hierarchical': 
                                                                {
                                                                 'enabled':True,
                                                                 'sortMethod': 'directed',
                                                                 'parentCentralization':True,
                                                                 'direction':'UD',
                                                                 'blockShifting':True,
                                                                }},
                                        'interaction':{'zoomView':False,
                                                        'dragNodes':False,
                                                        'dragView':False
                                                      },
                                }
                        ),
                    ])

@app.callback(
    Output('net', 'options'),
#    [Input('color', 'value')]
    )
def myfun(x):
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)
