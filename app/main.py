
from fastapi import FastAPI, HTTPException
from typing import List
from app.schemas import Profile, ProfileCreate, ProfileUpdate
from uuid import UUID, uuid4
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
profiles = []
uuid = uuid4()
print(uuid)

@app.get("/")
def root():
    return {"message": "Profile Manager API is running 🚀"}

@app.post("/profiles/", response_model=Profile, status_code=201)
def create_profile(profile: ProfileCreate):
    uuid = uuid4()
    new_profile = Profile(id=uuid, **profile.dict())
    profiles.append(new_profile)
    return new_profile

@app.get("/profiles/", response_model=List[Profile])
def list_profiles():
    return profiles

@app.get("/profiles/{profile_id}", response_model=Profile)
def get_profile(profile_id: UUID):
    for profile in profiles:
        if profile.id == profile_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/profiles/{profile_id}", response_model=Profile)
def update_profile(profile_id: UUID, profile_update: ProfileUpdate):
    for idx, profile in enumerate(profiles):
        if profile.id == profile_id:
            current_profile = profile.dict()
            update_fields = profile_update.dict(exclude_unset=True)
            current_profile.update(update_fields)
            updated_profile = Profile(**current_profile)
            profiles[idx] = updated_profile
            return updated_profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.delete("/profiles/{profile_id}", status_code=204)
def delete_profile(profile_id: UUID):
    for idx, profile in enumerate(profiles):
        if profile.id == profile_id:
            del profiles[idx]
            return
    raise HTTPException(status_code=404, detail="Profile not found")

