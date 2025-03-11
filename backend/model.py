from pydantic import BaseModel, Field
from dependencies.dbschema import PyObjectId


class EmbeddingData(BaseModel):
    uuid: PyObjectId = Field(..., description="The uniquely generated id of the user")
    strpath : str = Field(..., description="The storage path of the file which is to be processed")

class SearchQuery(BaseModel):
    uuid: PyObjectId = Field(..., description="The uniquely generated id of the user")
    query_str: str = Field(..., description="The query string which is to be provided to search through the embeddings")