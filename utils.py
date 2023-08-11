import pickle
import numpy as np
import config
import json

class FitnessTracker():
    def __init__(self):
        pass

    def get_data(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model=pickle.load(f)

        with open(config.SCALER_FILE_PATH, "rb") as f:
            self.scaler=pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json = json.load(f)


    def get_predicted_insight(self,TotalSteps,TotalDistance,TrackerDistance,LoggedActivitiesDistance,VeryActiveDistance,LightActiveDistance,SedentaryActiveDistance,VeryActiveMinutes,FairlyActiveMinutes,LightlyActiveMinutes,SedentaryMinutes,DayOfTheWeek,TotalActiveMinutes,TotalActiveHours):

        self.get_data()

        DayOfTheWeek = self.json["DayOfTheWeek"][DayOfTheWeek]
        
    
        TotalSteps,TotalDistance,TrackerDistance,LoggedActivitiesDistance,VeryActiveDistance,LightActiveDistance,SedentaryActiveDistance,VeryActiveMinutes,FairlyActiveMinutes,LightlyActiveMinutes,SedentaryMinutes,TotalActiveMinutes,TotalActiveHours = self.scaler.transform([[TotalSteps,TotalDistance,TrackerDistance,LoggedActivitiesDistance,VeryActiveDistance,LightActiveDistance,SedentaryActiveDistance,VeryActiveMinutes,FairlyActiveMinutes,LightlyActiveMinutes,SedentaryMinutes,TotalActiveMinutes,TotalActiveHours]])[0]
            
        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0,0] =TotalSteps
        test_array[0,1] =TotalDistance
        test_array[0,2] =TrackerDistance
        test_array[0,3] =LoggedActivitiesDistance
        test_array[0,4] =VeryActiveDistance
        test_array[0,5] =LightActiveDistance
        test_array[0,6] =SedentaryActiveDistance
        test_array[0,7] =VeryActiveMinutes
        test_array[0,8] =FairlyActiveMinutes
        test_array[0,9] =LightlyActiveMinutes
        test_array[0,10] =SedentaryMinutes
        test_array[0,11] =DayOfTheWeek
        test_array[0,12] =TotalActiveMinutes
        test_array[0,13] =TotalActiveHours

        predicted_insight = self.model.predict(test_array)[0]
        return predicted_insight

        #if ('DayOfTheWeek' == 'DayOfTheWeek' and 'total_distance' >= 10000 and 'calories_burnt' >= 1500):
        #    return jsonify({'message': f'Active on {DayOfTheWeek}'})
        #else:
        #    return jsonify({'message': f'Not Active on {DayOfTheWeek}'})
