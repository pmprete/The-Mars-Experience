using UnityEngine;
using UnityEngine.UI;
using System.Collections;

[RequireComponent(typeof(AudioSource))]
public class displayUI : MonoBehaviour
{

    public string Title;
    public string Line1;
    public string Line2;
    public string Line3;
    public Text myText;

    public bool displayInfo = false;

    // Use this for initialization
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseOver()
    {
        displayInfo = true;
    }

    void OnMouseEnter()
    {
        AudioSource audio = GetComponent<AudioSource>();
        if(audio != null)
            audio.Play();

    }

    void OnMouseExit()

    {
        displayInfo = false;

    }

        void OnGUI()
    {
        if(displayInfo == true)
        {
            var rect = new Rect(15, Screen.height - 120, Screen.width, 80);
            GUI.skin.label.alignment = TextAnchor.UpperCenter;
            GUI.skin.label.fontSize = 25;
            GUI.Label(rect, Title);
            rect = new Rect(15, Screen.height - 95, Screen.width, 80);
            GUI.skin.label.fontSize = 15;
            GUI.Label(rect, Line1 + "\n" + Line2 + "\n" + Line3);

            var aTexture = GetComponent<GUITexture>();
            GUI.DrawTexture(new Rect(20, 20, 200, 200), aTexture.texture, ScaleMode.StretchToFill, true);

        }
    }



}