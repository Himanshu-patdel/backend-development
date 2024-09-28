# import json
# import os
# import time
# import requests
# import httpx
# import asyncio
# import pytest
# import logging
# from monolith.drafting.models import DraftingSearchParameters, NoveltyRequest

 

# # Load JSON data from file
# def load_json_data(filename):
#     with open(filename, 'r') as file:
#         return json.load(file)

# data_file = os.path.join(os.path.dirname(__file__), 'sample.json')
# json_data = load_json_data(data_file)


# def save_results_to_json(data, filename):
#     with open(filename, 'a') as file:
#         json.dump(data, file, indent=4)
        
# results_file = os.path.join(os.path.dirname(__file__), 'results.json')
# results={}
# # Base URL endpoints
# base_url = "http://0.0.0.0:8000/api"


# # Generate PDF file
# async def test_generate_pdf(search_id):
#     url = f"{base_url}/v1/file_generator/drafting_export_file?search_id={search_id}"
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         response = await client.get(url)
#         assert response.status_code == 200
#         print("Generating PDF:", response.json())
#     return response.json()
 
 

# # Main test function to process each JSON object sequentially
# @pytest.mark.asyncio
# async def test_generate_drafting():
#     for json_id, json_info in json_data.items():
#         # Generate novelty
#         type = "DETECT"
#         expected_status = 200
#         expected_message = "Novelty detected."

#         payload = NoveltyRequest(
#             invention=json_info['invention_disclosure'],
#             reference_novelty="Prior Art Reference XYZ",
#             user_message="",
#             is_regenerate=True,
#         ).dict()

#         response = requests.post(
#             f"{base_url}/v1/drafting/novelty?type={type}", json=payload
#         )
        
#         logging.info(f"Json ID: {json_id},Status Code: {response.status_code}")
#         assert response.status_code == expected_status
#         response_json = response.json()
#         assert response_json["status"] == "success"
#         assert response_json["message"] == expected_message
        
       
#         # Generate Drafting Search Parameters
#         search_payload = DraftingSearchParameters(
#             drafting_type="DRAFTING",
#             jurisdiction="US",
#             project_title=json_info['project_title'],
#             abstract="This invention relates to an advanced thermal management system designed to enhance the cooling efficiency of high-performance electronic devices.",
#             novelty=response_json["data"]["novelty"],
#             invention_disclosure=json_info['invention_disclosure'], 
#             problem_statement=json_info['problem_statement'],
#             keyfeatures="1. Novel heat dissipation mechanism.\n2. Enhanced cooling efficiency.",
#             uploaded_classes=["Thermal Management Systems", "Electronic Cooling Solutions"],
#             uploaded_ucids=["US7370044B2", "US1234567B1"],
#         ).dict()

#         search_response = requests.post(f"{base_url}/v1/drafting/create_draft", json=search_payload)
#         assert search_response.status_code == 200
#         search_response_json = search_response.json()
#         search_id = search_response_json["search_id"]
        
#         results = {
#         "search_id": search_id,
#         # "total_time_create_draft": total_time_create_draft,
#         "generate_part_times": {}
#         }
        
#         # Generate drafting parts
#         async def generate_drafting_part(part):
#             start_time = time.time()
#             url = f"{base_url}/v1/drafting/generate?part={part}&search_id={search_id}"
#             async with httpx.AsyncClient(timeout=120.0) as client:
#                 response = await client.get(url)
#                 elapsed_time = time.time() - start_time
#                 return response

#         # Generate CLAIMS and FIGURES sequentially
#         start_time = time.time()
#         claims_response = await generate_drafting_part("CLAIMS")
#         total_time_claims = time.time() - start_time
#         assert claims_response.status_code == 200 
#         print(f"Claims generated successfully for Json ID: {json_id}.")
#         results["generate_part_times"]["CLAIMS"] = total_time_claims
        
#         start_time = time.time()
#         figures_response = await generate_drafting_part("FIGURES")
#         total_time_figures = time.time() - start_time
#         assert figures_response.status_code == 200 
#         results["generate_part_times"]["FIGURES"] = total_time_figures
#         print(f"Figures generated successfully for Json ID: {json_id}.")

#         # Generate other parts in parallel
#         parts = ["FIGURE_LIST", "ABSTRACT", "SUMMARY", "DESCRIPTION", "TECHNICAL_FIELD"]
#         tasks = [generate_drafting_part(part) for part in parts]
#         results = await asyncio.gather(*tasks)

#         for result in results:
#             assert result.status_code == 200

#         # Generate TITLE and BACKGROUND sequentially
#         title_response = await generate_drafting_part("TITLE")
#         assert title_response.status_code == 200 

#         background_response = await generate_drafting_part("BACKGROUND")
#         assert background_response.status_code == 200 
#         # generate pdf file 
        
        
#         # Generate PDF after all parts are done
#         pdf_response = await test_generate_pdf(search_id)
#         print(f"PDF generated for Json ID: {json_id} with response: {pdf_response}")

#         # print(f"PDF generated for Json ID: {json_id} with response: {pdf_response}")

#         save_results_to_json(results, results_file)
        
        

 





import json
import os
import time
import requests
import httpx
import asyncio
import pytest
import logging
from monolith.drafting.models import DraftingSearchParameters, NoveltyRequest

# Load JSON data from file
def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

data_file = os.path.join(os.path.dirname(__file__), 'sample.json')
json_data = load_json_data(data_file)

def save_results_to_json(data, filename):
    
    with open(filename, 'a') as file:
        json.dump(data , file, indent=4)

results_file = os.path.join(os.path.dirname(__file__), 'results.json')
overall_results = {}  # To store cumulative results across iterations

# Base URL endpoints
base_url = "http://0.0.0.0:8000/api"

# Generate PDF file
@pytest.mark.asyncio
async def test_generate_pdf(search_id):
    url = f"{base_url}/v1/file_generator/drafting_export_file?search_id={search_id}"
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.get(url)
        assert response.status_code == 200
        print("Generating PDF:", response.json())
    return response.json()

# Main test function to process each JSON object sequentially
@pytest.mark.asyncio
async def test_generate_drafting():
    for json_id, json_info in json_data.items():
        # Generate novelty
        type = "DETECT"
        expected_status = 200
        expected_message = "Novelty detected."

        payload = NoveltyRequest(
            invention=json_info['invention_disclosure'],
            reference_novelty="Prior Art Reference XYZ",
            user_message="",
            is_regenerate=True,
        ).dict()
        s=time.time()
        response = requests.post(
            f"{base_url}/v1/drafting/novelty?type={type}", json=payload
        )
        last=time.time()-s
        
        logging.info(f"Json ID: {json_id},Status Code: {response.status_code}")
        assert response.status_code == expected_status
        response_json = response.json()
        assert response_json["status"] == "success"
        assert response_json["message"] == expected_message
        json_results = {
            "search_id": "",
            "generate_part_times": {"Novelty" : last}
        }
        
        # Generate Drafting Search Parameters
        search_payload = DraftingSearchParameters(
            drafting_type="DRAFTING",
            jurisdiction="US",
            project_title=json_info['project_title'],
            abstract="This invention relates to an advanced thermal management system designed to enhance the cooling efficiency of high-performance electronic devices.",
            novelty=response_json["data"]["novelty"],
            invention_disclosure=json_info['invention_disclosure'], 
            problem_statement=json_info['problem_statement'],
            keyfeatures="1. Novel heat dissipation mechanism.\n2. Enhanced cooling efficiency.",
            uploaded_classes=["Thermal Management Systems", "Electronic Cooling Solutions"],
            uploaded_ucids=["US7370044B2", "US1234567B1"],
        ).dict()

        search_response = requests.post(f"{base_url}/v1/drafting/create_draft", json=search_payload)
        assert search_response.status_code == 200
        search_response_json = search_response.json()
        search_id = search_response_json["search_id"]
        
        # Initialize results for this JSON ID
        json_results["search_id"]=search_id
        
        # Generate drafting parts
        async def generate_drafting_part(part):
            start_time = time.time()
            url = f"{base_url}/v1/drafting/generate?part={part}&search_id={search_id}"
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.get(url)
                elapsed_time = time.time() - start_time
                return response, elapsed_time

        # Generate CLAIMS and FIGURES sequentially
        claims_response, total_time_claims = await generate_drafting_part("CLAIMS")
        assert claims_response.status_code == 200 
        print(f"Claims generated successfully for Json ID: {json_id}.")
        json_results["generate_part_times"]["CLAIMS"] = total_time_claims
        
        figures_response, total_time_figures = await generate_drafting_part("FIGURES")
        assert figures_response.status_code == 200 
        json_results["generate_part_times"]["FIGURES"] = total_time_figures
        print(f"Figures generated successfully for Json ID: {json_id}.")

        # Generate other parts in parallel
        parts = ["FIGURE_LIST", "ABSTRACT", "SUMMARY", "DESCRIPTION", "TECHNICAL_FIELD"]
        tasks = [generate_drafting_part(part) for part in parts]
        part_results = await asyncio.gather(*tasks)

        for part_name, (part_result, elapsed_time) in zip(parts, part_results):
            assert part_result.status_code == 200
            json_results["generate_part_times"][part_name] = elapsed_time

        # Generate TITLE and BACKGROUND sequentially
        title_response, _ = await generate_drafting_part("TITLE")
        assert title_response.status_code == 200 

        background_response, _ = await generate_drafting_part("BACKGROUND")
        assert background_response.status_code == 200 

        # Generate PDF after all parts are done
        pdf_response = await test_generate_pdf(search_id)
        print(f"PDF generated for Json ID: {json_id} with response: {pdf_response}")

        # Save results for this JSON ID
        json_results["pdf_link"]=pdf_response["file_path"]
        print(pdf_response["file_path"])
        overall_results[json_id] = json_results

        # Save results to file
        save_results_to_json(json_results, results_file)
