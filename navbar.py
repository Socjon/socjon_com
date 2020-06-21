import dash_bootstrap_components as dbc
import dash_html_components as html


# def Navbar():
#     navbar = dbc.NavbarSimple(
#         children=[
#             # dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
#             # dbc.NavItem(dbc.NavLink("About", href="/about")),
#             dbc.NavItem(dbc.NavLink("About", href="/about")),
#             dbc.DropdownMenu(
#                 nav=True,
#                 in_navbar=True,
#                 label="Portfolio",
#                 children=[
#                     dbc.DropdownMenuItem("Auditors Aid", href="/auditor"),
#                     dbc.DropdownMenuItem("How I built this site", href="/dash_101"),
#                     dbc.DropdownMenuItem(divider=True),
#                     dbc.DropdownMenuItem("Entry 3"),
#                 ],
#             ),
#             dbc.NavItem(dbc.NavLink("Blog", href="https://medium.com/@socjon")),
#             dbc.NavItem(dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/tyler-jonathan/")),
#
#         ],
#         brand="Home",
#         brand_href="/home",
#         sticky="left",
#     )
#     return navbar
#

def Navbar():
    sidebar = html.Div(
        [
            html.H2("Sidebar"),
            html.Hr(),
            html.P("A simple sidebar layout with navigation links"),
            html.Ul(
                [

                    dbc.DropdownMenu(
                                        nav=True,
                                        in_navbar=True,
                                        label="Portfolio",
                                        children=[
                                            dbc.DropdownMenuItem("Auditors Aid", href="/auditor"),
                                            dbc.DropdownMenuItem("How I built this site", href="/dash_101"),
                                            dbc.DropdownMenuItem(divider=True),
                                            dbc.DropdownMenuItem("Entry 3"),
                                        ],
                    ),
                    dbc.NavLink("About", href="/about"),
                    dbc.NavLink("Blog", href="/blog"),
                    dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/tyler-jonathan/")
                ], className="navLink"
            ),
        ],
        className="sidenav",
    )
    return sidebar