import inspect

SURROUND = ("You will be provided with a Python function enclosed with {{{ CODE }}} "
            "and a desired code change enclosed with {{{ CHANGE }}}.")
SINGLE_TASK = "Your task is to return a new Python function with the required change."

def get_user_prompt(func: callable, change: str) -> str:
    return f"""
    CHANGE: {{{{{ {change} }}}}}
    
    CODE: {{{{{ {inspect.getsource(func)} }}}}}
    
    REFACTORED CODE:
    """
def get_estimated_user_costs(prompts_data):
    costs = {}
    for entry in prompts_data:
        user = entry["user"]
        prompt = entry["prompt"]
        estimated_tokens = len(prompt) / 4  # Số 4 là hằng số chưa tối ưu
        cost = estimated_tokens * 0.0001    # Số 0.0001 là magic number

        if user not in costs:
            costs[user] = cost
        else:
            costs[user] += cost
    return costs

if __name__ == "__main__":
    print("--- THỰC THI LAB 4.2: REFACTORING VỚI 5S PROMPT ---")
    change_request = "Convert hard-coded integers to global constants and use dict.get()"

    # Tạo Prompt vật lý
    final_prompt = get_user_prompt(get_estimated_user_costs, change_request)
    print(f"PROMPT GỬI ĐẾN AI:\n{final_prompt}")