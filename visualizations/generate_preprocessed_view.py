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

    def generate_view_003(self):
        instance = V003.V003()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,11):
            instance.save_chart(i)

    def generate_view_004(self):
        instance = V004.V004()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,13):
            instance.save_chart(i)

    def generate_view_005(self):
        instance = V005.V005()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,25):
            instance.save_chart(i)

    def generate_view_006(self):
        instance = V006.V006()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,14):
            instance.save_chart(i)

    def generate_view_007(self):
        instance = V007.V007()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,5):
            instance.save_chart(i)
    
    def generate_view_008(self):
        instance = V008.V008()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,12):
            instance.save_chart(i)

    def generate_view_009(self):
        instance = V009.V009()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,6):
            instance.save_chart(i)

    def generate_view_010(self):
        instance = V010.V010()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,33):
            instance.save_chart(i)

    def generate_view_011(self):
        instance = V011.V011()
        instance.generate_dataset(rand_names=self._student_names)
        
        for i in range(1,6):
            instance.save_chart(i)

# instance = PreprocessedView()
# instance.random_data(20)
# instance.generate_view_001()
# instance.generate_view_002()
# instance.generate_view_003()
# instance.generate_view_004()
# instance.generate_view_005()
# instance.generate_view_006()
# instance.generate_view_007()
# instance.generate_view_008()
# instance.generate_view_009()
# instance.generate_view_010()
# instance.generate_view_011()