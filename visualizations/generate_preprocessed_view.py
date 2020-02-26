import pandas as pd
import numpy as np
import V001, V002, V003, V004, V005, V006, V007, V008, V009, V010, V011

class PreprocessedView:
    _student_names = pd.DataFrame()
    
    def __init__(self):
        pass
    
    def random_data(self, n_students=20):
        names = pd.read_csv("assets/names.csv")
        self._student_names = [names.group_name[np.random.randint(0,len(names.group_name)+1)] for n in range(0,n_students)]
        self._student_names.sort()

    def generate_view_001(self):
        instance = V001.V001()
        instance.generate_dataset(number_assigns=10, rand_names=self._student_names)
        
        for i in range(1,56):
            instance.save_chart(i)
    
    def generate_view_002(self):
        instance = V002.V002()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,19):
            instance.save_chart(i)

instance = PreprocessedView()
instance.random_data(20)
# instance.generate_view_001()
instance.generate_view_002()