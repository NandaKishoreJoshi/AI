from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-611421379590-611089748519-616494846662-9286d063eb89896128e76b298bd51195', #app verification token
							'xoxb-611421379590-613778656740-FhuJebSKecpTxWIsXX6DwRbp', # bot verification token
							'ACLczf2FkIMPAyeIfmgYhTYh', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))