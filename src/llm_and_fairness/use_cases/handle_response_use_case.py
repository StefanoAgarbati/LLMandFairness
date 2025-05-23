class HandleResponseUseCase:

    def __init__(self, tool_repository):
        self.tool_repository = tool_repository

    def handle(self, aresponse):
        has_calls = aresponse.has_calls()
        if not has_calls:
            #self.show_response(aresponse.get_message())
            return [aresponse]
        else:
            try:
            #tool_execution_message = ToolExecutionMessage()
            #tool_execution_message.append(amessage.get_message())
            #print("HandleResponseUC->handle->", aresponse.get_message())
                exec_results = self.execute_calls(aresponse.get_tool_calls())
                return exec_results
            except Exception:
                #print("HandleResponseUseCas->handle->exception raised->")
                aresponse.set_tool_calls_error(True)
                return [aresponse]
            #self.process_execution_result(exec_results)

    def execute_calls(self, tool_calls):
        exec_results = []
        for tool_call in tool_calls:
            tool = self.tool_repository.get_tool_by_name(tool_call.get_name())
            tool_exec_result = tool.execute(tool_call.get_data())
            #print("tool_exec_result: " , tool_exec_result.get_tool_name())
            #print("tool_exec_result: ", tool_exec_result.get_args())
            exec_results.append(tool_exec_result)
            #print("HandleResponseUC->execute_calls->")
        return exec_results
            #self.process_execution_result(exec_results)

    """def process_execution_result(self, exec_results):
        for result in exec_results:
            #tool_exec_message.append(result.get_result())
            self.process_tool_result(result)

        #self.send_message_to_chat(tool_exec_message)"""

    """def process_tool_result(self, tool_execution_result):
        tool_name = tool_execution_result.get_tool_name()
        match tool_name:
            case 'load_dataset':
                self.process_load_dataset(tool_execution_result)
            case 'get_distribution':
                self.process_get_distribution(tool_execution_result)
            case _:
                raise Exception("HandleResponseUseCase - process_tool_result() - the tool is not defined")
        #self.show_response(tool_execution_result.get_artifact())
        #self.show_response(tool_execution_result.get_content())"""

    """def process_load_dataset(self, tool_execution_result):
        self.show_response(tool_execution_result.get_artifact())
        self.show_response(tool_execution_result.get_content())"""

    def process_get_distribution(self, tool_execution_result):
        pass







