import CreateObjectByPath
from core.NegoTable import NegoTable
from core.Preference import Preference
from configurations import *
from core.StateInfo import StateInfo
from core.TimeLine import TimeLine


class BilateralSession:

    def __init__(self, protocol_name: str, analysis_man_name: str, deadline,
                 first_preference_name: str, second_preference_name: str,
                 party1_name: str, party2_name: str, domain_name: str):
        try:
            self.preference1 = Preference(domain_name, first_preference_name)
            self.party1 = CreateObjectByPath.get_object(AGENTS_PACKAGE_NAME, party1_name, self.preference1)

            self.preference2 = Preference(domain_name, second_preference_name)
            self.party2 = CreateObjectByPath.get_object(AGENTS_PACKAGE_NAME, party2_name, self.preference2)

            time_line = TimeLine(float(deadline))
            state_info = StateInfo(time_line=time_line, my_agent_offers=[], opponent_offers={})

            nego_table = NegoTable(parties=(self.party1, self.party2), state_info=state_info)

            self.protocol = CreateObjectByPath.get_object(PROTOCOL_PACKAGE_NAME, protocol_name, time_line, nego_table)

            self.analysis_man = CreateObjectByPath.get_object(ANALYSIS_PACKAGE_NAME, analysis_man_name,
                                                              self.party1, self.party2, nego_table, self.preference1,
                                                              self.preference2)

        except (ImportError, AttributeError) as e:
            raise ImportError('NegoSim could not import :)', e)

    def start_session(self):
        print('----------------- Negotiation Session -----------------')
        print(self.preference1.get_domain_name(), ',',self.preference2.get_domain_name(),' -> ', self.party1, '(', self.preference1.get_preference_name(), ')', ' Vs ', self.party2, '(',self.preference2.get_preference_name(), ')')
        print('-------------------------------------------------------')
        self.protocol.negotiate()
        print('----------------- Negotiation Result -----------------')
        print(self.analysis_man.get_analysis_data())
        print('------------------------------------------------------\n')
        self.analysis_man.save_analysis_data()

    def get_protocol(self):
        return self.protocol

    def get_analysis_man(self):
        return self.analysis_man