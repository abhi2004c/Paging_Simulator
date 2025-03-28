import plotly.graph_objects as go

def visualize_page_replacement(page_order):
    """
    Visualize the page replacement process using Plotly.
    """
    fig = go.Figure()
    for i, memory_state in enumerate(page_order):
        fig.add_trace(go.Scatter(x=[i] * len(memory_state), y=memory_state, mode='markers+lines', name=f'Time {i}'))

    fig.update_layout(
        title="Page Replacement Visualization",
        xaxis_title="Time",
        yaxis_title="Page",
        template="plotly_dark",
        showlegend=False
    )
    
    fig.show()

def visualize_page_faults(page_faults):
    """
    Display the number of page faults.
    """
    fig = go.Figure(data=[go.Bar(x=['Page Faults'], y=[page_faults], name='Page Faults')])
    fig.update_layout(title="Number of Page Faults", xaxis_title="Page Faults", yaxis_title="Count")
    fig.show()
