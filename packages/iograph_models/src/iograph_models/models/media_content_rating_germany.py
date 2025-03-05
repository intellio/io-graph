from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingGermany(BaseModel):
	movieRating: Optional[str | RatingGermanyMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingGermanyTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_germany_movies_type import RatingGermanyMoviesType
from .rating_germany_television_type import RatingGermanyTelevisionType

