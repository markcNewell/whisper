class LanguageModelOptions:
    model_name: str = "Stub"


class LanguageModel:
    """
    Language Model masks each value in turn and finds the probability that it is the correct value
    If there is another similar word which is really probable we can maybe return that one?
    """
    def __init__(self, options: LanguageModelOptions) -> None:
        self.options = options

    def evaluate(self, sentences: List[str]) -> List[float]:
        raise NotImplementedError()

class LanguageModelStub(LanguageModel):
    def __init__(self, options: LanguageModelOptions) -> None:
        super().__init__(options)

    def evaluate(self, sentences: List[str]) -> List[float]:
        return [np.random.random(len(sentence)) for sentence in sentences]