from typing import List, Optional

from pydantic import BaseModel
from datetime import date

class ModelSpendBase(BaseModel):
    model_name: str
    cell_A1: float
    cell_A2: float
    cell_A3: float
    cell_A4: float
    cell_A5: float
    cell_A6: float
    cell_A7: float

    class Config:
        orm_mode = True

class ModelSpendCreate(ModelSpendBase):
    pass

class ModelSpend(ModelSpendBase):
    id: int
    owner_id: int

class CampaignBase(BaseModel):
    brand: str

class CampaignCreate(CampaignBase):
    start_date: Optional[date]
    end_date: Optional[date]
    campaign_spend: float
    vehicle: str
    audience_size: int
    country: str
    objective: str
    passion_points: str

class Campaign(CampaignBase):
    id: int
    country: str
    items: List[ModelSpend] = []

    class Config:
        orm_mode = True

class ShowCampaign(BaseModel):
    id: int
    model_spends: List[ModelSpendBase] = []

    class Config:
        orm_mode = True

class ShowDataCard(BaseModel):
    id: int
    start_date: date
    end_date: date
    campaign_spend: float
    vehicle: str
    audience_size: int

    class Config:
        orm_mode = True

class CampaignSpendBase(BaseModel):
    uplift: float
    control_group_spend: float
    test_group_spend: float

    class Config:
        orm_mode = True

class CampaignSpendCreate(CampaignSpendBase):
    pass

class CampaignSpend(CampaignSpendBase):
    id: int
    owner_id: int

class ShowCampaignSpend(CampaignSpendBase):
    owner_id: int

class AgeSplitBase(BaseModel):
    cat_18_25: int
    cat_26_35: int
    cat_36_45: int
    others: int
    class Config:
        orm_mode = True

class AgeSplitCreate(AgeSplitBase):
    pass

class AgeSplit(AgeSplitBase):
    id: int
    owner_id: int

class ShowAgeSplit(AgeSplitBase):
    owner_id: int

class GenderSplitBase(BaseModel):
    male: int
    female: int
    class Config:
        orm_mode = True

class GenderSplitCreate(GenderSplitBase):
    pass

class GenderSplit(GenderSplitBase):
    id: int
    owner_id: int

class ShowGenderSplit(GenderSplitBase):
    owner_id: int