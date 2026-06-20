import os
import sys
import pandas as pd
from openai import OpenAI

def run_pipeline():
    # Fetch API key securely from environment configuration
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: Secure OpenAI API Key is missing.")
        sys.exit(1)
        
    client = OpenAI(api_key=api_key)

    # 1. Base business performance variables 
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales_INR":,
        "Target_INR": [500000, 500000, 500000, 500000, 500000, 500000]
    }
    df = pd.DataFrame(data)
    data_summary = df.to_string(index=False)

    # 2. Prompt engineering configuration
    prompt = f"""
    You are an expert financial analyst. Analyze this business performance data:
    {data_summary}

    Provide exactly two sentences summarizing:
    1. The overall growth trend and key breakthrough month.
    2. An actionable recommendation based on target vs. actual performance.
    Keep it strictly under 60 words total. Do not use markdown styling or bullet points.
    """

    print("Generating AI Insights...")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.3
        )
        ai_insight = response.choices.message.content.strip()
    except Exception as e:
        print(f"API Error: {e}")
        sys.exit(1)

    # 3. Inject AI analysis column and drop to staging file
    df['AI_Executive_Insight'] = ai_insight
    df.to_excel('automated_sales_data.xlsx', sheet_name='SalesData', index=False)
    print("Success! 'automated_sales_data.xlsx' created.")

if __name__ == "__main__":
    run_pipeline()