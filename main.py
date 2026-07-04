from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal

app = FastAPI(
    title="GigHub API -c027-01-0887/2024")

CATEGORIES = ["Marketing", "Data", "Consulting"]
CURRENCY = "KES"


class Gig(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=20, max_length=500)
    category: Literal["Marketing", "Data", "Consulting"]
    budget: float = Field(gt=0)
    currency: str
    status: Literal["Open", "In Progress", "Closed"]
    client_name: str = Field(min_length=2, max_length=50)


class GigCreate(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=20, max_length=500)
    category: Literal["Marketing", "Data", "Consulting"]
    budget: float = Field(gt=0)
    client_name: str = Field(min_length=2, max_length=50)


class GigUpdate(BaseModel):
    budget: Optional[float] = Field(default=None, gt=0)
    status: Optional[Literal["Open", "In Progress", "Closed"]] = None


gigs_db = [
    {
        "id": 1,
        "title": "Social Media Campaign",
        "description": "Manage a social media campaign for a retail business targeting new customers.",
        "category": "Marketing",
        "budget": 10000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "James Kariuki"
    },
    {
        "id": 2,
        "title": "Data Cleaning Project",
        "description": "Clean and organize customer data into a structured and accurate database.",
        "category": "Data",
        "budget": 12000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Mercy Wanjiru"
    },
    {
        "id": 3,
        "title": "Business Strategy Consulting",
        "description": "Provide consulting services to improve the startup's growth strategy.",
        "category": "Consulting",
        "budget": 25000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Peter Mwangi"
    },
    {
        "id": 4,
        "title": "SEO Optimization",
        "description": "Improve website visibility through search engine optimization techniques.",
        "category": "Marketing",
        "budget": 15000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Alice Njeri"
    },
    {
        "id": 5,
        "title": "Sales Data Analysis",
        "description": "Analyze company sales data and prepare comprehensive business reports.",
        "category": "Data",
        "budget": 18000.0,
        "currency": "KES",
        "status": "Closed",
        "client_name": "John Kamau"
    },
    {
        "id": 6,
        "title": "Market Research Study",
        "description": "Conduct market research to identify customer preferences and trends.",
        "category": "Marketing",
        "budget": 14000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Faith Chebet"
    },
    {
        "id": 7,
        "title": "Data Visualization Dashboard",
        "description": "Create dashboards that visualize important business performance metrics.",
        "category": "Data",
        "budget": 22000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Kevin Otieno"
    },
    {
        "id": 8,
        "title": "Financial Consulting",
        "description": "Advise a business on budgeting, financial planning and investment decisions.",
        "category": "Consulting",
        "budget": 30000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Grace Akinyi"
    },
    {
        "id": 9,
        "title": "Email Marketing Setup",
        "description": "Configure email marketing campaigns with automated customer follow-ups.",
        "category": "Marketing",
        "budget": 11000.0,
        "currency": "KES",
        "status": "Closed",
        "client_name": "Daniel Kiptoo"
    },
    {
        "id": 10,
        "title": "Customer Data Entry",
        "description": "Enter customer records accurately into the company's information system.",
        "category": "Data",
        "budget": 9000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Lucy Wairimu"
    },
    {
        "id": 11,
        "title": "HR Process Consulting",
        "description": "Review and improve recruitment and employee onboarding procedures.",
        "category": "Consulting",
        "budget": 28000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Samuel Kibet"
    },
    {
        "id": 12,
        "title": "Brand Awareness Campaign",
        "description": "Develop a campaign to improve the company's brand awareness and visibility.",
        "category": "Marketing",
        "budget": 17000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Rose Atieno"
    }
]

@app.get("/gigs/search")
def search_gigs(q: str):
    results = []

    for gig in gigs_db:
        if q.lower() in gig["title"].lower():
            results.append(gig)

    return results

@app.post("/gigs")
def create_gig(gig: GigCreate):

    new_gig = {
        "id": len(gigs_db) + 1,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": CURRENCY,
        "status": "Open",
        "client_name": gig.client_name
    }

    gigs_db.append(new_gig)

    return new_gig

@app.get("/gigs")
def get_gigs(
    category: Optional[str] = None,
    min_budget: Optional[float] = None,
    max_budget: Optional[float] = None
):
    results = gigs_db

    if category:
        results = [
            gig for gig in results
            if gig["category"].lower() == category.lower()
        ]

    if min_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] >= min_budget
        ]

    if max_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] <= max_budget
        ]

    return results

@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, update: GigUpdate):

    for gig in gigs_db:

        if gig["id"] == gig_id:

            if update.budget is not None:
                gig["budget"] = update.budget

            if update.status is not None:
                gig["status"] = update.status

            return gig

    raise HTTPException(status_code=404, detail="Gig not found")



@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig

    raise HTTPException(status_code=404, detail="Gig not found")


@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):

    for index, gig in enumerate(gigs_db):

        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)
            return deleted_gig

    raise HTTPException(status_code=404, detail="Gig not found")                         