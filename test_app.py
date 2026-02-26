from app import app

# 1. Test if the header is present
def test_header_is_present(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the header to render, then check if it exists
    dash_duo.wait_for_element("#header", timeout=10)
    
    # Check if the text displays exactly what is expected
    header_text = dash_duo.find_element("#header").text
    assert header_text == "Soul Foods: Pink Morsel Sales Visualiser"

# 2. Test if the visualisation is present
def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    
    # Wait for the graph to render
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# 3. Test if the region picker is present
def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    
    # Wait for the radio items to render
    dash_duo.wait_for_element("#region-picker", timeout=10)