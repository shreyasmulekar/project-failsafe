using System;
using System.Diagnostics;
using System.IO;
using System.Threading;
using System.Windows.Forms;

namespace ProjectFailsafeOrganizer
{
    static class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            try
            {
                string baseDir = AppDomain.CurrentDomain.BaseDirectory;
                string serverScript = Path.Combine(baseDir, "server.py");

                // Start python server in background
                ProcessStartInfo srvInfo = new ProcessStartInfo();
                srvInfo.FileName = "python";
                srvInfo.Arguments = "\"" + serverScript + "\"";
                srvInfo.WorkingDirectory = baseDir;
                srvInfo.UseShellExecute = true;
                srvInfo.WindowStyle = ProcessWindowStyle.Minimized;

                try
                {
                    Process.Start(srvInfo);
                    Thread.Sleep(1200); // Give server time to bind port 8000
                }
                catch (Exception)
                {
                    // If python is not on PATH, try standard py launcher
                    try
                    {
                        srvInfo.FileName = "py";
                        Process.Start(srvInfo);
                        Thread.Sleep(1200);
                    }
                    catch (Exception)
                    {
                        MessageBox.Show(
                            "Python was not detected on this machine.\nTo host a multi-team LAN server, please install Python 3.\n\nOpening in standalone offline station mode instead.",
                            "PROJECT FAILSAFE Notice",
                            MessageBoxButtons.OK,
                            MessageBoxIcon.Information
                        );
                        string htmlPath = Path.Combine(baseDir, "public", "index.html");
                        Process.Start(new ProcessStartInfo(new Uri(htmlPath).AbsoluteUri) { UseShellExecute = true });
                        return;
                    }
                }

                // Launch Edge or Chrome in app mode
                string[] browserPaths = new string[]
                {
                    @"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    @"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                };

                string chosenBrowser = null;
                foreach (string p in browserPaths)
                {
                    if (File.Exists(p)) { chosenBrowser = p; break; }
                }

                string targetUrl = "http://localhost:8000";
                if (chosenBrowser != null)
                {
                    Process.Start(new ProcessStartInfo(chosenBrowser, string.Format("--app=\"{0}\" --window-size=1300,850", targetUrl)));
                }
                else
                {
                    Process.Start(new ProcessStartInfo(targetUrl) { UseShellExecute = true });
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error starting organizer console: " + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
