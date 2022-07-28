from sqlalchemy import Float, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, unique=True, index=True)
    country = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    campaign_spend = Column(Float)
    vehicle = Column(String)
    audience_size = Column(Integer)
    objective = Column(String)
    passion_points = Column(String)

    model_spends = relationship("ModelSpend", back_populates="owner")
    campaign_spends = relationship("CampaignSpend", back_populates="owner")
    age_splits = relationship("AgeSplit", back_populates="owner")
    gender_splits = relationship("GenderSplit", back_populates="owner")

class ModelSpend(Base):
    __tablename__ = "model_spends"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, index=True)
    cell_A1 = Column(Float)
    cell_A2 = Column(Float)
    cell_A3 = Column(Float)
    cell_A4 = Column(Float)
    cell_A5 = Column(Float)
    cell_A6 = Column(Float)
    cell_A7 = Column(Float)
    owner_id = Column(Integer, ForeignKey("campaigns.id"))

    owner = relationship("Campaign", back_populates="model_spends")

class CampaignSpend(Base):
    __tablename__ = "campaign_spends"

    id = Column(Integer, primary_key=True, index=True)
    uplift = Column(Float)
    control_group_spend = Column(Float)
    test_group_spend = Column(Float)
    owner_id = Column(Integer, ForeignKey("campaigns.id"))

    owner = relationship("Campaign", back_populates="campaign_spends")

class AgeSplit(Base):
    __tablename__ = "age_splits"

    id = Column(Integer, primary_key=True, index=True)
    cat_18_25 = Column(Integer)
    cat_26_35 = Column(Integer)
    cat_36_45 = Column(Integer)
    others = Column(Integer)
    owner_id = Column(Integer, ForeignKey("campaigns.id"))

    owner = relationship("Campaign", back_populates="age_splits")

class GenderSplit(Base):
    __tablename__ = "gender_splits"

    id = Column(Integer, primary_key=True, index=True)
    male = Column(Integer)
    female = Column(Integer)
    owner_id = Column(Integer, ForeignKey("campaigns.id"))

    owner = relationship("Campaign", back_populates="gender_splits")