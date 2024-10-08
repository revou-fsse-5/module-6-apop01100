class Messages():
    
    @staticmethod
    def success_message(subject: str, method: str, id: None | int=None):
        if id is not None:
            return f"success {method.upper()} {subject} data id={id}"
        return f"success {method.upper()} {subject} data"
    
    @staticmethod
    def not_found_messages(subject: str, id: None | int=None):
        if id is not None:
            return f"not found {subject} id={id}"
        return f"not found {subject} data"