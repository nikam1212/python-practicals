import tkinter as tk
import time
import threading

class TrafficLightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulation")
        self.root.geometry("200x450")
        self.root.resizable(False, False)

        # Canvas to draw the traffic light housing
        self.canvas = tk.Canvas(root, width=180, height=430, bg="lightgray")
        self.canvas.pack(pady=10)

        # Draw background housing rectangle
        self.canvas.create_rectangle(20, 20, 160, 410, fill="#333333", width=2)

        # Draw the 3 light circles (default off state / dark color)
        self.red_light = self.canvas.create_oval(40, 40, 140, 140, fill="#4a0000", outline="black")
        self.yellow_light = self.canvas.create_oval(40, 160, 140, 260, fill="#4a4a00", outline="black")
        self.green_light = self.canvas.create_oval(40, 280, 140, 380, fill="#004a00", outline="black")

        # Control flag to stop the thread cleanly when closing the window
        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start the traffic light cycle loop in a separate background thread
        self.cycle_thread = threading.Thread(target=self.run_cycle, daemon=True)
        self.cycle_thread.start()

    def run_cycle(self):
        """Main loop that switches colors based on standard timing."""
        while self.running:
            # 1. RED LIGHT ON (Active for 5 seconds)
            if not self.running: break
            self.set_lights(red=True, yellow=False, green=False)
            time.sleep(5)

            # 2. GREEN LIGHT ON (Active for 4 seconds)
            if not self.running: break
            self.set_lights(red=False, yellow=False, green=True)
            time.sleep(4)

            # 3. YELLOW LIGHT ON (Active for 2 seconds)
            if not self.running: break
            self.set_lights(red=False, yellow=True, green=False)
            time.sleep(2)

    def set_lights(self, red, yellow, green):
        """Updates the visual canvas items with bright colors when active."""
        # Use safe configuration updates using itemconfig
        self.canvas.itemconfig(self.red_light, fill="#FF0000" if red else "#4a0000")
        self.canvas.itemconfig(self.yellow_light, fill="#FFFF00" if yellow else "#4a4a00")
        self.canvas.itemconfig(self.green_light, fill="#00FF00" if green else "#004a00")

    def on_close(self):
        """Safely stops the thread loop before exiting."""
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    app = TrafficLightApp(window)
    window.mainloop()
