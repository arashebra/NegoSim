from itertools import permutations
import CreateObjectByPath
from core.BilateralSession import BilateralSession
from controller import Controller
from configurations import *


class BilateralTournament:

    def __init__(self, protocol_name: str, analysis_man_name: str, Tournament_analysis_name: str, deadline,
                 agent_names: list, opponent_names: list, domain_names: list):

        self.__domain_names = domain_names
        self.__agent_names = agent_names
        self.__opponent_names = opponent_names
        self.__protocol_name = protocol_name
        self.__analysis_man_name = analysis_man_name
        self.__deadline = deadline
        self.__tournament_analysis_man = CreateObjectByPath.get_object(ANALYSIS_TOURNAMENT_PACKAGE_NAME,
                                                                       Tournament_analysis_name,
                                                                       agent_names)

    def get_tournament_analysis_man(self):
        return self.__tournament_analysis_man

    def start_tournament(self):
        ctrl = Controller()
        for domain_name in self.__domain_names:
            preferences_of_domain = ctrl.fetch_preferences_of_domain(domain_name)
            for preference_permutations in permutations(preferences_of_domain, 2):
                for party1_name in self.__agent_names:
                    for party2_name in self.__opponent_names:
                        if party1_name != party2_name:
                            bilateral_session = BilateralSession(protocol_name=self.__protocol_name,
                                                                 analysis_man_name=self.__analysis_man_name,
                                                                 deadline=self.__deadline,
                                                                 first_preference_name=preference_permutations[0],
                                                                 second_preference_name=preference_permutations[1],
                                                                 party1_name=party1_name,
                                                                 party2_name=party2_name,
                                                                 domain_name=domain_name)

                            bilateral_session.start_session()
                            self.__tournament_analysis_man.add_session_analysis_data(
                                bilateral_session.get_analysis_man().get_analysis_data())

        print('**************************** Final Result ****************************')
        print(self.__tournament_analysis_man.get_tournament_analysis_data())
        print('**********************************************************************')
        self.__tournament_analysis_man.save_analysis_data()

    def get_tournament_analysis_man(self):
        return self.__tournament_analysis_man
