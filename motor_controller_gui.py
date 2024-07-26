import wx
import os
import numpy as np
import matplotlib.pyplot as plt

wildcard = "CSV source (*.csv)|*.csv|" \
           "All files (*.*)|*.*"

class PlotFrame(wx.Frame):
    def __init__(self, parent, title, data):
        super().__init__(parent, title=title, size=(800, 600))
        self.data = data
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.plot(data)
        
    def plot(self, data):
        try:
            # Extract columns from the structured array
            time = data['time']
            velocity = data['velocity']
            
            plt.figure(figsize=(10, 6))
            plt.plot(time, velocity, label='Velocity vs. Time', color='b')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Velocity (rad/s)')
            plt.title('Velocity vs. Time Plot')
            plt.legend()
            plt.grid(True)
            plt.show()

        except Exception as e:
            wx.LogError(f"Failed to plot data: {e}")

    def onClose(self, event):
        # Ensure plt.close() is called when the wx window is closed
        plt.close('all')
        self.Destroy()

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((704, 778))
        self.SetTitle("Motor Driver Interface")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 0, wx.ALL | wx.EXPAND, 5)

        Port_Selection = wx.StaticText(self.panel_1, wx.ID_ANY, "Select Port")
        Port_Selection.SetForegroundColour(wx.Colour(0, 0, 0))
        Port_Selection.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_3.Add(Port_Selection, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.port_name = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.port_name.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_3.Add(self.port_name, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.select_port_button = wx.Button(self.panel_1, wx.ID_ANY, "Select")
        self.select_port_button.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_3.Add(self.select_port_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_13, 1, wx.EXPAND, 0)

        Acceleration = wx.StaticText(self.panel_1, wx.ID_ANY, u"Angular Acceleration (α)")
        Acceleration.SetForegroundColour(wx.Colour(0, 0, 0))
        Acceleration.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_13.Add(Acceleration, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.acceleration = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.acceleration.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_13.Add(self.acceleration, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.acceleration_units = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["rad / s^2"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.acceleration_units.SetSelection(0)
        sizer_13.Add(self.acceleration_units, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_12, 1, wx.EXPAND, 0)

        Velocity = wx.StaticText(self.panel_1, wx.ID_ANY, u"Angular Velocity (ω)")
        Velocity.SetForegroundColour(wx.Colour(0, 0, 0))
        Velocity.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_12.Add(Velocity, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.velocity = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.velocity.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_12.Add(self.velocity, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.velocity_units = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["rev/min (rpm)"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.velocity_units.SetSelection(0)
        sizer_12.Add(self.velocity_units, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_11, 1, wx.EXPAND, 0)

        Time = wx.StaticText(self.panel_1, wx.ID_ANY, "Time Limit (t)")
        Time.SetForegroundColour(wx.Colour(0, 0, 0))
        Time.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_11.Add(Time, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Value = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.Value.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_11.Add(self.Value, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.time_units = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["s"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.time_units.SetSelection(0)
        sizer_11.Add(self.time_units, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_14, 1, wx.EXPAND, 0)

        Load = wx.StaticText(self.panel_1, wx.ID_ANY, "Load")
        Load.SetForegroundColour(wx.Colour(0, 0, 0))
        Load.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_14.Add(Load, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Path = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.Path.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_14.Add(self.Path, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.browse_button = wx.Button(self.panel_1, wx.ID_ANY, "Browse")
        sizer_14.Add(self.browse_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Proceed_button = wx.Button(self.panel_1, wx.ID_ANY, "Proceed")
        self.Proceed_button.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Proceed_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_14.Add(self.Proceed_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_8, 1, wx.EXPAND, 0)

        self.Stop = wx.Button(self.panel_1, wx.ID_ANY, "Stop")
        self.Stop.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.Stop.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Stop.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.Stop, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        self.Start = wx.Button(self.panel_1, wx.ID_ANY, "Start")
        self.Start.SetBackgroundColour(wx.Colour(112, 219, 147))
        self.Start.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Start.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.Start, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_9, 1, wx.EXPAND, 0)

        self.Emergeny_Stop = wx.Button(self.panel_1, wx.ID_ANY, "Emergency\n     Stop!")
        self.Emergeny_Stop.SetMinSize((250, 100))
        self.Emergeny_Stop.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.Emergeny_Stop.SetForegroundColour(wx.Colour(0, 0, 0))
        self.Emergeny_Stop.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_9.Add(self.Emergeny_Stop, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 15)

        self.reset_button = wx.Button(self.panel_1, wx.ID_ANY, "Reset")
        self.reset_button.SetMinSize((98, 34))
        self.reset_button.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_9.Add(self.reset_button, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onOpenFile, self.browse_button)
        self.Bind(wx.EVT_BUTTON, self.onReset, self.reset_button)
        self.Bind(wx.EVT_BUTTON, self.onStart, self.Start)
        self.Bind(wx.EVT_BUTTON, self.onStop, self.Stop)
        self.Bind(wx.EVT_BUTTON, self.onEmergencyStop, self.Emergeny_Stop)
        self.Bind(wx.EVT_BUTTON, self.onSelectPort, self.select_port_button)
        self.Bind(wx.EVT_BUTTON, self.onProceed, self.Proceed_button)

        # Bind the EVT_TEXT event to the text fields for velocity and time limit
        self.Bind(wx.EVT_TEXT, self.onVelocityChange, self.velocity)
        self.Bind(wx.EVT_TEXT, self.onTimeChange, self.Value)
        # end wxGlade

    def onOpenFile(self, event):  # wxGlade: MyFrame.<event_handler>
        with wx.FileDialog(self, "Open CSV file", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # The user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.Path.SetValue(pathname)  # Update the Path text control with the selected file path

    def onReset(self, event):
        self.port_name.SetValue("")
        self.acceleration.SetValue("")
        self.velocity.SetValue("")
        self.Value.SetValue("")
        self.Path.SetValue("")
        self.acceleration_units.SetSelection(0)
        self.velocity_units.SetSelection(0)
        self.time_units.SetSelection(0)

    def onStart(self, event):
        port_name = self.port_name.GetValue()
        acceleration = self.acceleration.GetValue()
        velocity = self.velocity.GetValue()
        time_limit = self.Value.GetValue()
        load_path = self.Path.GetValue()
        acc_units = self.acceleration_units.GetStringSelection()
        vel_units = self.velocity_units.GetStringSelection()
        time_units = self.time_units.GetStringSelection()
        
        print(f"Starting with port: {port_name}, acceleration: {acceleration} {acc_units}, velocity: {velocity} {vel_units}, time limit: {time_limit} {time_units}, load path: {load_path}")

    def onStop(self, event):
        print("Stopping the motor.")

    def onEmergencyStop(self, event):
        print("Emergency stop activated!")

    def onSelectPort(self, event):
        port_name = self.port_name.GetValue()
        print(f"Port selected: {port_name}")

    def onVelocityChange(self, event):
        self.calculate_acceleration()

    def onTimeChange(self, event):
        self.calculate_acceleration()

    def calculate_acceleration(self):
        try:
            velocity = float(self.velocity.GetValue())
            time_limit = float(self.Value.GetValue())
            if time_limit != 0:
                acceleration = (velocity * ((2 * np.pi) / 60)) / time_limit
                self.acceleration.SetValue(f"{acceleration:.5f}")
            else:
                self.acceleration.SetValue("")
        except ValueError:
            self.acceleration.SetValue("") 

    def onProceed(self, event):
        pathname = self.Path.GetValue()
        if pathname:
            try:
                data = np.genfromtxt(pathname, delimiter=',', names=True)
                print("Data loaded successfully:")
                print(data)
                if 'time' not in data.dtype.names or len(data.dtype.names) != 2:
                    wx.LogError("CSV file must contain 'time' column and one additional data column.")
                    return

                plot_frame = PlotFrame(self, "Plot", data)
                plot_frame.Show()
            except IOError:
                wx.LogError("Cannot open file '%s'." % pathname)
            except Exception as e:
                wx.LogError(f"An error occurred: {e}")


# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
