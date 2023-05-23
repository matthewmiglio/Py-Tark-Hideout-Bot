import PySimpleGUI as sg

from .stats import stat_box, stats

info_text = """1. Tarkov must be set to windowed mode
2. Program must be run as administrator.
3. Crafts must be favorited in their respective stations
4. Hideout lights must be set on using the fluorescent lights

Matthew Miglio, Martin Miglio - Nov 2022"""

instructions_text = """The bot farms crafts for lavatory,
water collector, bitcoin farm, medstation, and workbench.

The bot farms cordura, purified water, bitcoins, pile of meds, and green gunpowder. Favorite these crafts in each station.
"""

# defining various things that r gonna be in the gui.
main_layout = [
    [
        sg.Frame(
            layout=[[sg.Text(info_text, size=(35, None))]],
            title="Info",
            relief=sg.RELIEF_SUNKEN,
            expand_x=True,
        ),
    ],
    # directions
    [
        sg.Frame(
            layout=[[sg.Text(instructions_text, size=(35, None))]],
            title="Directions",
            relief=sg.RELIEF_SUNKEN,
            expand_x=True,
        ),
    ],
    [
        sg.Frame(
            layout=[
                [
                    sg.Text("'Bitcoin' Farming"),
                    sg.Checkbox("", key="bitcoin_checkbox", default=True),
                ],
                [
                    sg.Text("Lavatory 'Cordura' Farming"),
                    sg.Checkbox("", key="lavatory_checkbox", default=True),
                ],
                [
                    sg.Text("Medstation 'Pile of Meds' Farming"),
                    sg.Checkbox("", key="medstation_checkbox", default=True),
                ],
                [
                    sg.Text("'Purified Water' Farming"),
                    sg.Checkbox("", key="water_checkbox", default=True),
                ],
                [
                    sg.Text("Workbench 'Green Gunpowder' Farming"),
                    sg.Checkbox("", key="workbench_checkbox", default=True),
                ],
                [
                    sg.Text("Scav Case Farming"),
                    sg.Checkbox("", key="scav_case_checkbox", default=True),
                ],
                [
                    sg.Text("Scav Case Type"),
                    sg.DropDown(['Moonshine', 'Intel', '95000', '15000', '2500'], default_value='2500', key='scav_case_type')
                ]
            ],
            title="Job List",
            relief=sg.RELIEF_SUNKEN,
            expand_x=True,
        ),
    ],
    # stats
    [
        sg.Frame(layout=stats, title="Stats", relief=sg.RELIEF_SUNKEN, expand_x=True),
    ],
    # buttons
    [
        sg.Frame(
            layout=[
                [
                    sg.Column(
                        [
                            [
                                sg.Button("Start"),
                                sg.Button("Stop", disabled=True),
                                sg.Checkbox(
                                    text="Auto-start",
                                    key="autostart",
                                    default=False,
                                    enable_events=True,
                                ),
                            ]
                        ],
                        element_justification="left",
                        expand_x=True,
                    ),
                    sg.Column(
                        [
                            [
                                sg.Button("Help"),
                                sg.Button("Issues?", key="issues-link"),
                                sg.Button("Donate"),
                            ]
                        ],
                        element_justification="right",
                        expand_x=True,
                    ),
                ],
            ],
            title="Controls",
            relief=sg.RELIEF_SUNKEN,
            expand_x=True,
        ),
    ],
    [
        stat_box("time_since_start", size=(7, 1)),
        sg.InputText(
            "Idle",
            key="message",
            use_readonly_for_disable=True,
            disabled=True,
            text_color="blue",
            expand_x=True,
        ),
    ],
    # https://www.paypal.com/donate/?business=YE72ZEB3KWGVY&no_recurring=0&item_name=Support+my+projects%21&currency_code=USD
]

# a list of all the keys that contain user configuration
# user_config_keys = ["rows_to_target", "remove_offers_timer", "autostart"]
user_config_keys = [
    # "rows_to_target",
    # "remove_offers_timer",
    "autostart",
    'bitcoin_checkbox',
    'lavatory_checkbox',
    'medstation_checkbox',
    'water_checkbox',
    'workbench_checkbox',
    'scav_case_checkbox',
    'scav_case_type',
]

# list of button and checkbox keys to disable when the bot is running
disable_keys = user_config_keys + ["Start"]
