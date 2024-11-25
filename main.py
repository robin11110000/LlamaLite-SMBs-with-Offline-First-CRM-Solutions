from fastapi import FastAPI

# Simulating the Llama model function for generating responses
def generate_response(prompt: str):
    # Replace this with actual model code or logic
    return f"Generated response for: {prompt}"

# Function to generate a follow-up message
def generate_follow_up(customer_name: str, last_interaction: str):
    prompt = f"Write a follow-up message for {customer_name} based on their last interaction: {last_interaction}"
    return generate_response(prompt)

# This is the FastAPI app instance
app = FastAPI()

# Endpoint for sending follow-up messages
@app.post("/follow_up")
def send_follow_up(customer_name: str, last_interaction: str):
    message = generate_follow_up(customer_name, last_interaction)
    return {"message": message}
