class GlobalDebugConfig:
    debug_mode = False

    @classmethod
    def set_debug_mode(cls):
        cls.debug_mode = True

    @classmethod
    def unset_debug_mode(cls):
        cls.debug_mode = False
