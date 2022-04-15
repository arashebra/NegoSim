from core.AbstractAnalysisMan import AbstractAnalysisMan
from core.AbstractTournamentAnalysisMan import AbstractTournamentAnalysisMan
import time
import pickle


class AnalysisTournament1(AbstractTournamentAnalysisMan):

    def __init__(self, session_analysis_man: AbstractAnalysisMan):
        self.session_analysis_man = session_analysis_man
        self.__tournament_analysis_data = {}

    def get_tournament_analysis_data(self) -> dict:
        '''
        :return: a dict like {
                                'AVG utility1': 0.89,
                                'AVG utility2': 0.75,
                                'AVG socialwelfare': 1.64
                              }
        '''
        session_analysis_dataset = self.get_session_analysis_dataset()
        i = 1
        for session_analysis_data in session_analysis_dataset:
            for key, value in session_analysis_data.items():
                if key not in self.__tournament_analysis_data:
                    self.__tournament_analysis_data[key] = value
                else:
                    self.__tournament_analysis_data[key] = (value + (self.__tournament_analysis_data[key] * i)) / (
                                i + 1)
                    i = i + 1
        return self.__tournament_analysis_data

    def save_analysis_data(self):
        '''
        This method saves data in logs folder
        '''
        file_name = 'TournamentData_pickled' + str(time.time_ns())
        tournament_data = open(f'./TournamentLogs/{file_name}', 'ab')
        data = self.__tournament_analysis_data if len(self.__tournament_analysis_data) > 0 else None
        pickle.dump(data, tournament_data)
        tournament_data.close()
