from abc import ABC, abstractmethod


class AbstractTournamentAnalysisMan(ABC):

    def __init__(self, agent_names: list):
        self.__agent_names = agent_names
        self.__session_analysis_dataset = []  # list of session analysis data

    def get_agent_names(self):
        return self.__agent_names

    def add_session_analysis_data(self, session_analysis_data):
        self.__session_analysis_dataset.append(session_analysis_data)

    def get_session_analysis_dataset(self):
        return self.__session_analysis_dataset

    @abstractmethod
    def get_tournament_analysis_data(self) -> dict:
        '''
        :return: a dict like {
                                'utility1': 0.89,
                                'utility2': 0.75,
                                'socialwelfare': 1.64
                              }
        '''
        raise NotImplementedError()

    @abstractmethod
    def save_analysis_data(self):
        '''
        This method saves data in logs folder
        '''
        raise NotImplementedError()
