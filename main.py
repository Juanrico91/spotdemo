from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/campaigns/", response_model=schemas.Campaign)
def create_campaign(campaign: schemas.CampaignCreate, db: Session = Depends(get_db)):
    db_campaign = crud.get_campaign_by_brand(db, brand=campaign.brand)
    if db_campaign:
        raise HTTPException(status_code=400, detail="brand already registered")
    return crud.create_campaign(db=db, campaign=campaign)


@app.get("/campaigns/", response_model=List[schemas.Campaign])
def read_campaigns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    campaigns = crud.get_campaigns(db, skip=skip, limit=limit)
    return campaigns


@app.get("/campaigns/{campaign_id}", response_model=schemas.ShowCampaign)
def read_campaign(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign = crud.get_campaign(db, campaign_id=campaign_id)
    if db_campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign


@app.post("/campaigns/{campaign_id}/model_spends/", response_model=schemas.ModelSpend)
def create_model_spend_for_campaign(
    campaign_id: int, model_spend: schemas.ModelSpendCreate, db: Session = Depends(get_db)
):
    return crud.create_campaign_model_spend(db=db, model_spend=model_spend, campaign_id=campaign_id)


@app.get("/model_spends/", response_model=List[schemas.ModelSpend])
def read_model_spends(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    model_spends = crud.get_model_spends(db, skip=skip, limit=limit)
    return model_spends

@app.post("/campaigns/{campaign_id}/campaign_spends/", response_model=schemas.CampaignSpend)
def create_campaign_spend(
    campaign_id: int, campaign_spend: schemas.CampaignSpendCreate, db: Session = Depends(get_db)
):
    return crud.create_campaign_spend(db=db, campaign_spend=campaign_spend, campaign_id=campaign_id)

@app.get("/campaign_spends/{campaign_id}", response_model=schemas.ShowCampaignSpend)
def read_campaign_spend(campaign_id: int, db: Session = Depends(get_db)):
    db_campaign_spend = crud.get_campaign_spend(db, campaign_id=campaign_id)
    if db_campaign_spend is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_campaign_spend

@app.get("/datacard/{campaign_id}", response_model=schemas.ShowDataCard)
def read_datacard(campaign_id: int, db: Session = Depends(get_db)):
    db_datacard = crud.get_datacard(db, campaign_id=campaign_id)
    if db_datacard is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_datacard

@app.post("/campaigns/{campaign_id}/age_splits/", response_model=schemas.AgeSplit)
def create_age_split(
    campaign_id: int, age_split: schemas.AgeSplitCreate, db: Session = Depends(get_db)
):
    return crud.create_age_split(db=db, age_split=age_split, campaign_id=campaign_id)

@app.get("/age_split/{campaign_id}", response_model=schemas.ShowAgeSplit)
def read_age_split(campaign_id: int, db: Session = Depends(get_db)):
    db_age_split = crud.get_age_split(db, campaign_id=campaign_id)
    if db_age_split is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_age_split

@app.post("/campaigns/{campaign_id}/gender_splits/", response_model=schemas.GenderSplit)
def create_gender_split(
    campaign_id: int, gender_split: schemas.GenderSplitCreate, db: Session = Depends(get_db)
):
    return crud.create_gender_split(db=db, gender_split=gender_split, campaign_id=campaign_id)

@app.get("/gender_split/{campaign_id}", response_model=schemas.ShowGenderSplit)
def read_gender_split(campaign_id: int, db: Session = Depends(get_db)):
    db_gender_split = crud.get_gender_split(db, campaign_id=campaign_id)
    if db_gender_split is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return db_gender_split