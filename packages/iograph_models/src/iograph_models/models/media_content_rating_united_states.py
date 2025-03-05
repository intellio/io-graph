from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingUnitedStates(BaseModel):
	movieRating: Optional[str | RatingUnitedStatesMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingUnitedStatesTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_united_states_movies_type import RatingUnitedStatesMoviesType
from .rating_united_states_television_type import RatingUnitedStatesTelevisionType

