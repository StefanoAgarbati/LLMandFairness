class ExecuteToolCallUseCase:

    def __init__(self, tool_repository):
        self.tool_repository = tool_repository

    def execute_tool_calls(self, tool_calls):
        exec_results = []
        for tool_call in tool_calls:
            tool = self.tool_repository.get_tool_by_name(tool_call.get_name())
            tool_exec_result = tool.execute(tool_call.get_data())
            exec_results.append(tool_exec_result)
            self.process_execution_result(exec_results)

    def process_execution_result(self, exec_results):
        for result in exec_results:
            self.process_tool_result(result)

    def process_tool_result(self, tool_execution_result):
        tool_name = tool_execution_result.get_tool_name()
        match tool_name:
            case 'load_dataset':
                self.process_load_dataset(tool_execution_result)

    def process_load_dataset(self, tool_execution_result):
        #self.show_response(tool_execution_result.get_artifact())
        #self.show_response(tool_execution_result.get_content())
        pass