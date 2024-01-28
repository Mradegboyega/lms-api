import fastapi

router = fastapi.APIRouter()

@router.get("/sections/{id}")
async def read_section(id: int):
    """
    Get information about a specific section.

    Parameters:
        - id (int): The ID of the section.

    Returns:
        dict: A dictionary containing information about the section.
    """
    return {"courses": []}

@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks(id: int):
    """
    Get content blocks associated with a specific section.

    Parameters:
        - id (int): The ID of the section.

    Returns:
        dict: A dictionary containing information about content blocks in the section.
    """
    return {"courses": []}

@router.get("/content-blocks/{id}")
async def read_content_blocks(id: int):
    """
    Get information about a specific content block.

    Parameters:
        - id (int): The ID of the content block.

    Returns:
        dict: A dictionary containing information about the content block.
    """
    return {"courses": []}
