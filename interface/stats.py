import PySimpleGUI as sg

from .theme import THEME

sg.theme(THEME)


def stat_box(stat_name: str, size=(5, 1)):
    return sg.Text(
        "0",
        key=stat_name,
        relief=sg.RELIEF_SUNKEN,
        text_color="blue",
        size=size,
    )


stats_title = [
    [
        [
            sg.Text("Workbench Starts: "),
        ],
        [
            sg.Text("Workbench Collects"),
        ],
        [
            sg.Text("Bitcoin Collects"),
        ],
        [
            sg.Text("Lavatory Starts"),
        ],
        [
            sg.Text("Lavatory Collects"),
        ],
    ],
    [
        [
            sg.Text("Medstation Starts"),
        ],
        [
            sg.Text("Medstation Collects"),
        ],
        [
            sg.Text("Water Filters"),
        ],
        [
            sg.Text("Water Collects"),
        ],
        [
            sg.Text("Restarts"),
        ],
        [
            sg.Text("Profit"),
        ],
    ],
]


stats_values = [
    [
        [
            stat_box("workbench_starts"),
        ],
        [
            stat_box("workbench_collects"),
        ],
        [
            stat_box("bitcoin_collects"),
        ],
        [
            stat_box("lavatory_starts"),
        ],
        [
            stat_box("lavatory_collects"),
        ],
    ],
    [
        [
            stat_box("medstation_starts"),
        ],
        [
            stat_box("medstation_collects"),
        ],
        [
            stat_box("water_filters"),
        ],
        [
            stat_box("water_collects"),
        ],
        [
            stat_box("restarts"),
        ],
        [
            stat_box("profit"),
        ],
    ],
]

stats = [
    [
        sg.Column(stats_title[0], element_justification="right"),
        sg.Column(stats_values[0], element_justification="left"),
        sg.Column(stats_title[1], element_justification="right"),
        sg.Column(stats_values[1], element_justification="left"),
    ]
]
