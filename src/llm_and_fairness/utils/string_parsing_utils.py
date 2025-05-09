import ast
import json


class StringParsingUtils:

    @staticmethod
    def from_json_to_dict(json_string):
        json_string = StringParsingUtils.remove_prefix_and_suffix(json_string, "{", "}")
        json_string = json_string.replace("'", '"')
        print("from_json_to_dict->json_string->",json_string)
        json_dict = json.loads(json_string)
        return json_dict

    @staticmethod
    def from_string_to_list(list_string):
        return StringParsingUtils.from_string_to_type(list_string)

    @staticmethod
    def from_string_to_dict(dict_string):
        return StringParsingUtils.from_string_to_type(dict_string)

    @staticmethod
    def from_string_to_type(type_string):
        return ast.literal_eval(type_string)

    @staticmethod
    def get_function_name_from_string(function_string):
        expr = ast.parse(function_string, mode="eval")

        function_name = expr.body.func.id
        return function_name

    @staticmethod
    def get_function_params_from_string(function_string):
        expr = ast.parse(function_string, mode="eval")

        args = {}
        for keyword in expr.body.keywords:
            key = keyword.arg
            value = ast.literal_eval(keyword.value)
            args[key] = value
        return args

    @staticmethod
    def from_function_string_to_dict(function_string):
        function_name = StringParsingUtils.get_function_name_from_string(function_string)
        function_args = StringParsingUtils.get_function_params_from_string(function_string)
        function_dict = {"name": function_name, "args": function_args}
        return function_dict

    @staticmethod
    def remove_prefix_and_suffix(a_string, prefix_sep, suffix_sep):
        a_string = a_string.strip()
        a_string = a_string.rpartition(suffix_sep)
        a_string = a_string[0] + a_string[1]
        a_string = a_string.partition(prefix_sep)
        a_string = a_string[1] + a_string[2]
        return a_string

    @staticmethod
    def test_from_function_string_to_dict():
        function_string = "nome_funzione(param1=10, param2=[12,'gino'])"
        res = StringParsingUtils.from_function_string_to_dict(function_string)
        print(res)

    @staticmethod
    def test_get_function_params_from_string():
        function_string = "nome_funzione(param1=10, param2=[12,'gino'])"
        res = StringParsingUtils.get_function_params_from_string(function_string)
        print(res)

    @staticmethod
    def test_from_string_to_dict():
        dict_string = """{
            "tool_calls": [
                {
                    "name": "func1",
                    "args": {
                        "a1": "v1",
                        "a2": "v2"
                    }
                },
                {
                    "name": "func2",
                    "args": {
                        "a1": "v1"
                    }
                }
            ]
        }"""
        res = StringParsingUtils.from_string_to_dict(dict_string)
        print(res)

#StringParsingUtils.test_from_string_to_dict()
#StringParsingUtils.test_get_function_params_from_string()
#StringParsingUtils.test_from_function_string_to_dict()