using UnityEngine;

public class WrapWorld : MonoBehaviour {
    
	void OnTriggerExit (Collider player) {
	    var postion = player.transform.position;
        Debug.Log("Player entered the trigger");
        Debug.Log("Position x :" + postion.x);
        Debug.Log("Position y :" + postion.y);
        Debug.Log("Position z :" + postion.z);
        if (postion.x > 490)
        {
            postion.x = 10;
        }
        if (postion.z > 490)
        {
            postion.z = 10;
        }

        if (postion.x < 10)
        {
            postion.x = 490;
        }
        if (postion.z < 10)
        {
            postion.z = 490;
        }

        postion.y = 20;
        player.transform.position = postion;
    }
}
