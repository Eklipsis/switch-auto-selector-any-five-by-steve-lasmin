class SwitchAutoSelectorAnyFive:
    """
    Auto-selects exactly one active signal from 5 optional ANY inputs.
    Raises a red-node error if zero or more than one input carries data.

    Use case: Wire multiple candidate sources, then bypass or mute all
    except the one you want active. The node finds the lone active path
    automatically.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "input_1": ("*", {}),
                "input_2": ("*", {}),
                "input_3": ("*", {}),
                "input_4": ("*", {}),
                "input_5": ("*", {}),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "select"
    CATEGORY = "utils"
    DESCRIPTION = (
        "Auto-selects exactly one active signal from 5 optional ANY inputs. "
        "Bypass or mute all sources except one. Red-node error if 0 or 2+ signals are active."
    )

    INPUT_TOOLTIPS = {
        "input_1": "Optional ANY input. Disconnect, bypass, or mute if not used. Must be None when inactive.",
        "input_2": "Optional ANY input. Disconnect, bypass, or mute if not used. Must be None when inactive.",
        "input_3": "Optional ANY input. Disconnect, bypass, or mute if not used. Must be None when inactive.",
        "input_4": "Optional ANY input. Disconnect, bypass, or mute if not used. Must be None when inactive.",
        "input_5": "Optional ANY input. Disconnect, bypass, or mute if not used. Must be None when inactive.",
    }

    OUTPUT_TOOLTIPS = {
        "output": "The single active signal selected from the 5 inputs. Type matches the active input.",
    }

    def select(self, input_1=None, input_2=None, input_3=None, input_4=None, input_5=None):
        inputs = [
            ("input_1", input_1),
            ("input_2", input_2),
            ("input_3", input_3),
            ("input_4", input_4),
            ("input_5", input_5),
        ]

        active = [(name, value) for name, value in inputs if value is not None]

        if len(active) == 0:
            raise ValueError(
                "[Switch Auto Selector (ANY Five)] No active signal detected. "
                "All 5 inputs are None (disconnected, bypassed, or muted). "
                "Connect exactly one active source."
            )

        if len(active) > 1:
            active_names = ", ".join(name for name, _ in active)
            raise ValueError(
                f"[Switch Auto Selector (ANY Five)] Multiple active signals detected on: {active_names}. "
                f"Only one input may carry data at a time. Bypass or mute the other sources."
            )

        return (active[0][1],)


NODE_CLASS_MAPPINGS = {
    "SwitchAutoSelectorAnyFive": SwitchAutoSelectorAnyFive,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SwitchAutoSelectorAnyFive": "Switch Auto Selector (ANY Five) by Steve Lasmin",
}
