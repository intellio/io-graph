# generated by datamodel-codegen:
#   filename:  https://github.com/microsoftgraph/msgraph-metadata/raw/refs/heads/master/openapi/v1.0/openapi.yaml
#   timestamp: 2025-02-01T01:07:47+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, RootModel


class ODataCountResponse(RootModel[int]):
    root: int


class ReferenceUpdate(BaseModel):
    field_odata_id: Optional[str] = None
    field_odata_type: Optional[str] = None


class ReferenceCreate(BaseModel):
    field_odata_id: Optional[str] = None


class ReferenceNumeric(Enum):
    field_inf = '-INF'
    inf = 'INF'
    na_n = 'NaN'


class BaseCollectionPaginationCountResponse(BaseModel):
    field_odata_count: Optional[int] = None
    field_odata_next_link: Optional[str] = None


class BaseDeltaFunctionResponse(BaseModel):
    field_odata_next_link: Optional[str] = None
    field_odata_delta_link: Optional[str] = None


class StringCollectionResponse(BaseCollectionPaginationCountResponse):
    value: Optional[List[str]] = None
