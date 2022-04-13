from itertools import permutations
from core.BilateralSession import BilateralSession
from controller import Controller


class BilateralTournament:

    def __init__(self, protocol_name: str, analysis_man_name: str, deadline,
                 party1_names: tuple, party2_names: tuple, domain_names: tuple):

        ctrl = Controller()
        for domain_name in domain_names:
            preferences_of_domain = ctrl.fetch_preferences_of_domain(domain_name)
            for preference_permutations in permutations(preferences_of_domain, 2):
                for party1_name in party1_names:
                    for party2_name in party2_names:
                        if party1_name != party2_name:
                            bilateral_session = BilateralSession(protocol_name=protocol_name,
                                                                 analysis_man_name=analysis_man_name,
                                                                 deadline=deadline,
                                                                 first_preference_name=preference_permutations[0],
                                                                 second_preference_name=preference_permutations[1],
                                                                 party1_name=party1_name,
                                                                 party2_name=party2_name,
                                                                 domain_name=domain_name)
                            bilateral_session.start_session()
