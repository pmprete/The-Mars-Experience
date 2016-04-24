using UnityEngine;

public class WrapWorld : MonoBehaviour {
    
	void OnTriggerExit (Collider player) {
	    var position = player.transform.position;
        var boxCollider = (BoxCollider)this.gameObject.GetComponent(typeof(BoxCollider));
        var boxCollaiderSize = boxCollider.size;
        var terrainPosition = Terrain.activeTerrain.transform.position;
        Debug.Log("Player entered the trigger");
        Debug.Log("Position x :" + position.x);
        Debug.Log("Position y :" + position.y);
        Debug.Log("Position z :" + position.z);
        Debug.Log("terrain position");
        Debug.Log("Position x :" + terrainPosition.x);
        Debug.Log("Position y :" + terrainPosition.y);
        Debug.Log("Position z :" + terrainPosition.z);
        Debug.Log("box colaider size");
        Debug.Log("Position x :" + boxCollaiderSize.x);
        Debug.Log("Position y :" + boxCollaiderSize.y);
        Debug.Log("Position z :" + boxCollaiderSize.z);
        if (position.x >= boxCollaiderSize.x)
        {
            position.x = terrainPosition.x + 10;
        }
        if (position.z >= boxCollaiderSize.z)
        {
            position.z = terrainPosition.z + 10;
        }

        if (position.x <= terrainPosition.x + 5)
        {
            position.x = boxCollaiderSize.x -1;
        }
        if (position.z <= terrainPosition.z + 5)
        {
            position.z = boxCollaiderSize.z - 1;
        }
        
        position.y = Terrain.activeTerrain.SampleHeight(position);
        player.transform.position = position;
    }
}
