'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''

    first_line = "<span style='font-family:Roboto Slab; font-weight:bold'>Neighborhood</span>: %{y}"
    second_line = "<span style='font-family:Roboto Slab; font-weight:bold'>Year</span>: %{x}"
    third_line = "<span style='font-family:Roboto Slab; font-weight:bold'>Trees planted</span>: %{z}"
    third_line += "<extra></extra>"

    return "<br>".join([first_line, second_line, third_line])


def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    
    first_line = "<span style='font-family:Roboto Slab; font-weight:bold'>Date</span>: %{x}"
    second_line = "<span style='font-family:Roboto Slab; font-weight:bold'>Trees</span>: %{y}"
    second_line += "<extra></extra>"

    return "<br>".join([first_line, second_line])

