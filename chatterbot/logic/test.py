from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        print(kwargs.get('age'))

    def can_process(self, statement):
        #print(dir(statement))
        #print(chatbot.name)
        #print(self.chatbot.name)
        #print(self.chatbot.age)
        #print(dir(self))
        #print(statement.search_text)
        print(dir(statement))
        print(statement.get_tags())
        print(type(statement))
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)

        # For this example, we will just return the input as output
        selected_statement = input_statement
        selected_statement.confidence = confidence

        return selected_statement
