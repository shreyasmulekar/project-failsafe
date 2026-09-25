using System;
using System.Diagnostics;
using System.IO;
using System.Net;
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

                // Start python server in background if not already responding
                string probeUrl = "http://127.0.0.1:8000/api/status";
                bool alreadyRunning = IsServerOnline(probeUrl, 600);

                if (!alreadyRunning)
                {
                    ProcessStartInfo srvInfo = new ProcessStartInfo();
                    srvInfo.FileName = "python";
                    srvInfo.Arguments = "\"" + serverScript + "\"";
                    srvInfo.WorkingDirectory = baseDir;
                    srvInfo.UseShellExecute = true;
                    srvInfo.WindowStyle = ProcessWindowStyle.Minimized;

                    try
                    {
                        Process.Start(srvInfo);
                    }
                    catch (Exception)
                    {
                        try
                        {
                            srvInfo.FileName = "py";
                            Process.Start(srvInfo);
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

                    // Poll up to 10 seconds for Python server to become ready
                    for (int i = 0; i < 40; i++)
                    {
                        Thread.Sleep(250);
                        if (IsServerOnline(probeUrl, 400)) break;
                    }
                }

                // Launch Edge or Chrome in app mode targeting 127.0.0.1 (avoids IPv6 localhost mismatch)
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

                string targetUrl = "http://127.0.0.1:8000/admin.html";
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

        static bool IsServerOnline(string url, int timeoutMs)
        {
            try
            {
                HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
                req.Timeout = timeoutMs;
                req.Method = "GET";
                using (HttpWebResponse resp = (HttpWebResponse)req.GetResponse())
                {
                    return resp.StatusCode == HttpStatusCode.OK;
                }
            }
            catch
            {
                return false;
            }
        }
    }
}
