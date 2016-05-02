

def mplt_setup(obj):
    obj.tight_layout()
    obj.margins(0.02)
    obj.margins(0.02)
    obj.minorticks_on()
    obj.grid(b=True, which='minor', color='w', linestyle=':')
    obj.tight_layout()