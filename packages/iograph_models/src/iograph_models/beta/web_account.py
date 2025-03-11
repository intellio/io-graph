from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WebAccount(BaseModel):
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
	description: Optional[str] = Field(alias="description",default=None,)
	service: Optional[ServiceInformation] = Field(alias="service",default=None,)
	statusMessage: Optional[str] = Field(alias="statusMessage",default=None,)
	thumbnailUrl: Optional[str] = Field(alias="thumbnailUrl",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)

from .allowed_audiences import AllowedAudiences
from .identity_set import IdentitySet
from .inference_data import InferenceData
from .identity_set import IdentitySet
from .person_data_sources import PersonDataSources
from .profile_source_annotation import ProfileSourceAnnotation
from .service_information import ServiceInformation

