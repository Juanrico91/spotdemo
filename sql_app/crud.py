from sqlalchemy.orm import Session

from . import models, schemas


def get_campaign(db: Session, campaign_id: int):
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()

def get_campaign_by_brand(db: Session, brand: str):
    return db.query(models.Campaign).filter(models.Campaign.brand == brand).first()

def get_campaigns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Campaign).offset(skip).limit(limit).all()

def create_campaign(db: Session, campaign: schemas.CampaignCreate):
    db_campaign = models.Campaign(
        brand=campaign.brand,
        start_date=campaign.start_date,
        end_date=campaign.end_date,
        country=campaign.country,
        campaign_spend=campaign.campaign_spend,
        vehicle=campaign.vehicle,
        audience_size=campaign.audience_size,
        objective=campaign.objective,
        passion_points=campaign.passion_points
        )
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

def get_model_spends(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ModelSpend).offset(skip).limit(limit).all()

def create_campaign_model_spend(db: Session, model_spend: schemas.ModelSpendCreate, campaign_id: int):
    db_model_spend = models.ModelSpend(**model_spend.dict(), owner_id=campaign_id)
    db.add(db_model_spend)
    db.commit()
    db.refresh(db_model_spend)
    return db_model_spend

def get_campaign_spend(db: Session, campaign_id: int):
    return db.query(models.CampaignSpend).filter(models.CampaignSpend.owner_id == campaign_id).first()

def create_campaign_spend(db: Session, campaign_spend: schemas.CampaignSpendCreate, campaign_id: int):
    db_campaign_spend = models.CampaignSpend(**campaign_spend.dict(), owner_id=campaign_id)
    db.add(db_campaign_spend)
    db.commit()
    db.refresh(db_campaign_spend)
    return db_campaign_spend

def get_datacard(db: Session, campaign_id: int):
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()

def create_age_split(db: Session, age_split: schemas.AgeSplitCreate, campaign_id: int):
    db_age_split = models.AgeSplit(**age_split.dict(), owner_id=campaign_id)
    db.add(db_age_split)
    db.commit()
    db.refresh(db_age_split)
    return db_age_split

def get_age_split(db: Session, campaign_id: int):
    return db.query(models.AgeSplit).filter(models.AgeSplit.owner_id == campaign_id).first()

def create_gender_split(db: Session, gender_split: schemas.GenderSplitCreate, campaign_id: int):
    db_gender_split = models.GenderSplit(**gender_split.dict(), owner_id=campaign_id)
    db.add(db_gender_split)
    db.commit()
    db.refresh(db_gender_split)
    return db_gender_split

def get_gender_split(db: Session, campaign_id: int):
    return db.query(models.GenderSplit).filter(models.GenderSplit.owner_id == campaign_id).first()