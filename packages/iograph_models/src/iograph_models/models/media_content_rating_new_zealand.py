from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingNewZealand(BaseModel):
	movieRating: Optional[str | RatingNewZealandMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingNewZealandTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_new_zealand_movies_type import RatingNewZealandMoviesType
from .rating_new_zealand_television_type import RatingNewZealandTelevisionType

