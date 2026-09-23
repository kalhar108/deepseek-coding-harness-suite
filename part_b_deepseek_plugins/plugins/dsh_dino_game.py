"""
DSH PLUGIN 2 (From Scratch): Floating Dino Jumping Game UI Widget
Hot-loaded in Creator Mode to demonstrate UI slot overlay synthesis (shell.overlay).
"""

class DinoGamePlugin:
    def __init__(self):
        self.plugin_id = "dsh-dino-game"
        self.name = "Dinosaur Jumping Game Overlay"
        self.ui_slot = "shell.overlay"
        self.score = 0
        self.is_running = True

    def render_html_widget(self) -> str:
        return f"""
<div id="dsh-dino-widget" style="position: fixed; bottom: 20px; right: 20px; width: 220px; background: #1e1e2e; color: #cdd6f4; border: 2px solid #89b4fa; border-radius: 12px; padding: 12px; font-family: sans-serif; box-shadow: 0 8px 24px rgba(0,0,0,0.4); z-index: 1000;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="font-size: 14px; color: #89b4fa;">🦖 DSH Dino Runner</strong>
        <span style="font-size: 11px; background: #313244; padding: 2px 6px; border-radius: 4px;">Score: {self.score}</span>
    </div>
    <div style="height: 60px; background: #11111b; border-radius: 6px; position: relative; overflow: hidden; display: flex; align-items: flex-end; padding: 4px;">
        <span id="dino-char" style="font-size: 24px; position: absolute; bottom: 4px; left: 10px; transition: bottom 0.2s;">🦖</span>
        <span style="font-size: 18px; position: absolute; bottom: 4px; right: 20px;">🌵</span>
    </div>
    <button onclick="alert('Dino Jumped!')" style="margin-top: 8px; width: 100%; background: #89b4fa; color: #11111b; border: none; padding: 6px; border-radius: 6px; font-weight: bold; cursor: pointer;">JUMP (Space)</button>
</div>
"""
