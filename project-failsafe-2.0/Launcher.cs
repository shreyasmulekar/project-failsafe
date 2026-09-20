using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

namespace ProjectFailsafe2
{
    static class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            try
            {
                string baseDir = AppDomain.CurrentDomain.BaseDirectory;
                string htmlPath = Path.Combine(baseDir, "index.html");

                if (!File.Exists(htmlPath))
                {
                    htmlPath = Path.Combine(baseDir, "aditi_os_2.html");
                }

                if (!File.Exists(htmlPath))
                {
                    MessageBox.Show(
                        "Could not locate 'index.html'.\nPlease ensure ProjectFailsafe2.exe is kept inside the project-failsafe-2.0 folder.",
                        "PROJECT FAILSAFE 2.0 - File Not Found",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error
                    );
                    return;
                }

                string fileUri = new Uri(htmlPath).AbsoluteUri;

                // Priority paths for Edge or Chrome in app mode
                string[] browserPaths = new string[]
                {
                    @"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
                    @"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    @"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                    Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), @"Microsoft\Edge\Application\msedge.exe"),
                    Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), @"Google\Chrome\Application\chrome.exe")
                };

                string chosenBrowser = null;
                foreach (string p in browserPaths)
                {
                    if (File.Exists(p))
                    {
                        chosenBrowser = p;
                        break;
                    }
                }

                if (chosenBrowser != null)
                {
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = chosenBrowser;
                    // --app creates a dedicated native desktop window without browser bars, tabs, or address bar
                    psi.Arguments = string.Format("--app=\"{0}\" --window-size=1400,900", fileUri);
                    Process.Start(psi);
                }
                else
                {
                    // Fallback to default system browser
                    ProcessStartInfo psi = new ProcessStartInfo();
                    psi.FileName = fileUri;
                    psi.UseShellExecute = true;
                    Process.Start(psi);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error starting application: " + ex.Message, "PROJECT FAILSAFE 2.0 Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
