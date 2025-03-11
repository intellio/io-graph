from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WorkPosition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedAudiences: Optional[AllowedAudiences | str] = Field(alias="allowedAudiences",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	inference: Optional[InferenceData] = Field(alias="inference",default=None,)
	isSearchable: Optional[bool] = Field(alias="isSearchable",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	source: Optional[PersonDataSources] = Field(alias="source",default=None,)
	sources: Optional[list[ProfileSourceAnnotation]] = Field(alias="sources",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	colleagues: Optional[list[RelatedPerson]] = Field(alias="colleagues",default=None,)
	detail: Optional[PositionDetail] = Field(alias="detail",default=None,)
	isCurrent: Optional[bool] = Field(alias="isCurrent",default=None,)
	manager: Optional[RelatedPerson] = Field(alias="manager",default=None,)

from .allowed_audiences import AllowedAudiences
from .identity_set import IdentitySet
from .inference_data import InferenceData
from .identity_set import IdentitySet
from .person_data_sources import PersonDataSources
from .profile_source_annotation import ProfileSourceAnnotation
from .related_person import RelatedPerson
from .position_detail import PositionDetail
from .related_person import RelatedPerson

