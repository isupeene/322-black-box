/*
  This file was copied from the provided
  Watchdog.java from professor Scott Dick
 */

import java.util.TimerTask;

class Watchdog extends TimerTask {
    private Thread watched;

    public Watchdog(Thread toWatch) {
	this.watched=toWatch;
    }

    public void run() {
	watched.stop();
    }
    
}
