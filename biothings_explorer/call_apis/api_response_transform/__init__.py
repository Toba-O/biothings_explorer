from .transformers.automat_transformer import AutomatTransformer
from .transformers.base_transformer import BaseTransformer
from .transformers.biolink_transformer import BioLinkTransformer
from .transformers.biothings_transformer import BioThingsTransformer
from .transformers.cord_transformer import CordTransformer
from .transformers.ctd_transformer import CTDTransformer
from .transformers.opentarget_transformer import OpenTargetTransformer
from .transformers.semmed_transformer import SemmedTransformer


class Transformer:
    def __init__(self, data):
        self.data = data
        self.route()

    def route(self):
        api = self.data["edge"]["association"]["api_name"]
        tags = self.data["edge"]["query_operation"]["tags"]
        if api.startswith("CORD"):
            self.tf = CordTransformer(self.data)
        elif api.startswith("SEMMED"):
            self.tf = SemmedTransformer(self.data)
        elif api == "BioLink API":
            self.tf = BioLinkTransformer(self.data)
        elif "automat" in tags:
            self.tf = AutomatTransformer(self.data)
        elif "biothings" in tags:
            self.tf = BioThingsTransformer(self.data)
        elif "ctd" in tags:
            self.tf = CTDTransformer(self.data)
        elif "opentarget" in tags:
            self.tf = OpenTargetTransformer(self.data)
        else:
            self.tf = BaseTransformer(self.data)

    def transform(self):
        return self.tf.transform()
